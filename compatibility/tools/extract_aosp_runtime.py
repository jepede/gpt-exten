#!/usr/bin/env python3
"""Extract a minimal Android ARM64/Bionic userspace from an OFFICIAL SDK system image.
The SDK image is NOT an NDK sysroot; it holds the actual runnable libc/linker.
"""
import hashlib, json, os, pathlib, re, shutil, subprocess, sys, tempfile, zipfile
from pathlib import Path

def log(*args): print(*args, flush=True)
def call(args, ok=True):
    p=subprocess.run(args,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
    log("+", " ".join(map(str,args)), "rc=", p.returncode, p.stdout[-1800:])
    if ok and p.returncode: raise RuntimeError(str(args))
    return p.stdout

ROOT=Path('runtime-work')
ROOT.mkdir(exist_ok=True)
IMAGE=ROOT/'system.img'
RAW=ROOT/'system.raw.img'
OUT=Path('release/sysroot')

def sdk_from_zip(zfile):
    with zipfile.ZipFile(zfile) as z:
        ims=[n for n in z.namelist() if n.endswith('/system.img') or n=='system.img']
        if not ims:
            raise RuntimeError("no system.img in official system-image ZIP")
        log("SDK_IMAGE_MEMBER",ims[0])
        with z.open(ims[0]) as src, IMAGE.open('wb') as dst:
            shutil.copyfileobj(src,dst,1024*1024)
    log('SDK_IMAGE_SIZE',IMAGE.stat().st_size)

def image_fs(path):
    import struct
    with path.open('rb') as disk:
        disk.seek(512)
        gpt=disk.read(512)
        if gpt[:8]==b'EFI PART':
            entries_lba=struct.unpack_from('<Q',gpt,72)[0]
            count=min(256,struct.unpack_from('<I',gpt,80)[0])
            entry_size=struct.unpack_from('<I',gpt,84)[0]
            partitions=[]
            for i in range(count):
                disk.seek(entries_lba*512+i*entry_size)
                ent=disk.read(entry_size)
                if not ent or ent[:16]==bytes(16):continue
                first,last=struct.unpack_from('<QQ',ent,32)
                name=ent[56:128].decode('utf-16le','ignore').rstrip(chr(0))
                partitions.append((name,first,last))
            log('GPT_PARTITIONS',partitions)
            super_parts=[p for p in partitions if p[0].lower()=='super']
            if not super_parts:raise RuntimeError('GPT has no dynamic super partition')
            name,start,end=super_parts[0]
            part=ROOT/'super.img'
            disk.seek(start*512)
            remaining=(end-start+1)*512
            with part.open('wb') as dst:
                while remaining:
                    data=disk.read(min(4*1024*1024,remaining))
                    if not data:raise IOError('unexpected end of GPT partition')
                    dst.write(data);remaining-=len(data)
            log('EXTRACTED_GPT_SUPER',part.stat().st_size)
            unpacked=ROOT/'logical'
            unpacked.mkdir(exist_ok=True)
            call(['lpunpack','-v',str(part),str(unpacked)])
            part.unlink()
            logical=sorted(unpacked.glob('system*.img'),key=lambda p:p.stat().st_size,reverse=True)
            if not logical:raise RuntimeError('super did not contain a system logical partition')
            path=logical[0]
            log('SELECTED_LOGICAL_SYSTEM',path,path.stat().st_size)
    hdr=path.open('rb').read(4)
    if hdr==bytes.fromhex('3aff26ed'):
        call(['simg2img',str(path),str(RAW)])
        path=RAW
    info=call(['file',str(path)])
    if 'EROFS' in info or 'erofs' in info:
        return 'erofs',path
    return 'ext4',path

class Reader:
    def __init__(self, image):
        self.mode,self.image=image_fs(image)
        self.fsdir=None
        if self.mode=='erofs':
            self.fsdir=ROOT/('extract_'+image.stem)
            self.fsdir.mkdir(parents=True,exist_ok=True)
            call(['fsck.erofs','--extract='+str(self.fsdir),str(self.image)])
    def listdir(self,p):
        if self.mode=='erofs':
            dest=self.fsdir/p.lstrip('/')
            return os.listdir(dest) if dest.is_dir() else []
        out=subprocess.run(['debugfs','-R','ls -p '+p,str(self.image)],capture_output=True,text=True)
        if out.returncode: return []
        names=[]
        for line in out.stdout.splitlines():
            parts=line.split('/')
            # debugfs -p entries: /inode/mode/uid/gid/name/type/
            if len(parts)>5 and parts[1].isdigit():
                names.append(parts[5])
        log('LIST',p,names[:80])
        return names
    def copy(self,source,dest):
        dest.parent.mkdir(parents=True,exist_ok=True)
        if self.mode=='erofs':
            s=self.fsdir/source.lstrip('/')
            if not s.is_file():return False
            shutil.copyfile(s,dest)
            return True
        p=subprocess.run(['debugfs','-R','dump -p '+source+' '+str(dest),str(self.image)],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
        if p.returncode!=0 or not dest.is_file() or dest.stat().st_size==0:
            dest.unlink(missing_ok=True)
            return False
        return True

def possible_paths(name):
    return ['/system/bin/'+name,'/bin/'+name,'/system/lib64/'+name,'/lib64/'+name,
            '/system_ext/lib64/'+name,'/product/lib64/'+name]

def extract_system(r):
    selected=['linker64','libc.so','libm.so','libdl.so','libc++.so','libstdc++.so','liblog.so',
              'libz.so','libbase.so','libunwindstack.so','libunwind.so','libandroid.so',
              'libnativehelper.so','libcutils.so','libutils.so','libbinder.so',
              'libcrypto.so','libssl.so','libclang_rt.asan-aarch64-android.so']
    count=0
    for filename in selected:
        for path in possible_paths(filename):
            dst=OUT/path.lstrip('/')
            if r.copy(path,dst):
                count+=1;log('EXTRACT_SYSTEM',path,dst.stat().st_size)
    for base in ['/apex','/system/apex']:
        candidates=[n for n in r.listdir(base) if re.match(r'^com\.android\.(runtime|art)(?:[.\-_].*)?\.(?:apex|capex)$',n)]
        # Some Android releases have apexes named com.android.runtime.apex directly.
        candidates+=['com.android.runtime.apex','com.android.runtime.capex','com.android.art.apex']
        for n in sorted(set(candidates)):
            dest=ROOT/'apex_packages'/n
            if r.copy(base+'/'+n,dest):
                log('EXTRACT_APEX_PACKAGE',base+'/'+n,dest.stat().st_size)
                if n.startswith('com.android.runtime'): unpack_apex(dest,'com.android.runtime')
                elif n.startswith('com.android.art'): unpack_apex(dest,'com.android.art')
    return count

def unpack_apex(apex,name):
    if not zipfile.is_zipfile(apex):
        log("NOT_ZIP_APEX",apex)
        return
    with zipfile.ZipFile(apex) as z:
        names=z.namelist()
        if 'original_apex' in names:
            inner=ROOT/(name+'.original.apex')
            with z.open('original_apex') as i, inner.open('wb') as o: shutil.copyfileobj(i,o)
            return unpack_apex(inner,name)
        payload=next((n for n in names if n.endswith('/apex_payload.img') or n=='apex_payload.img'),None)
        if not payload:
            log('APEX_NO_IMG',name,names[:20]);return
        raw=ROOT/(name.replace('.','_')+'.img')
        with z.open(payload) as i,raw.open('wb') as o: shutil.copyfileobj(i,o)
    r=Reader(raw)
    if name=='com.android.runtime':
        for fname in ['linker64','linker']:
            for s in ['/bin/'+fname,'/system/bin/'+fname]:
                dst=OUT/'apex'/name/'bin'/fname
                if r.copy(s,dst):
                    log('EXTRACT_RUNTIME_LINKER',dst,dst.stat().st_size)
                    if fname=='linker64':
                        # Compatibility symlink target physically present for QEMU interpreter.
                        t=OUT/'system/bin/linker64';t.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(dst,t)
                    break
        # Copy all Bionic libraries, including libc, libdl, libm and runtime helper libs.
        dirs=['/lib64/bionic','/lib64','/lib/bionic']
        for base in dirs:
            names=r.listdir(base)
            for fname in names:
                if not fname.endswith('.so') and '.so.' not in fname:continue
                s=base+'/'+fname;d=OUT/'apex'/name/base.lstrip('/')/fname
                if r.copy(s,d):log('EXTRACT_RUNTIME_LIB',s,d.stat().st_size)
        # Make usual /system/lib64 fallback for binary compatibility only if absent.
        libbase=OUT/'apex'/name/'lib64/bionic'
        for fname in ['libc.so','libdl.so','libm.so']:
            s=libbase/fname
            if s.exists():
                d=OUT/'system/lib64'/fname;d.parent.mkdir(parents=True,exist_ok=True)
                if not d.exists():shutil.copy2(s,d)
    else:
        for base in ['/lib64','/lib64/bionic']:
            for fname in r.listdir(base):
                if fname.endswith('.so'):
                    s=base+'/'+fname;d=OUT/'apex'/name/base.lstrip('/')/fname
                    if r.copy(s,d):log('EXTRACT_ART_LIB',s,d.stat().st_size)

def main():
    sdk_from_zip(Path(sys.argv[1]))
    r=Reader(IMAGE)
    extract_system(r)
    required=['system/bin/linker64','apex/com.android.runtime/lib64/bionic/libc.so',
              'apex/com.android.runtime/lib64/bionic/libdl.so']
    missing=[str(x) for x in required if not (OUT/x).is_file()]
    files=sorted(str(x.relative_to(OUT)) for x in OUT.rglob('*') if x.is_file())
    log("EXTRACTED_FILE_COUNT",len(files))
    log("MISSING_REQUIRED",missing)
    summary={"source_zip":sys.argv[1],"required_missing":missing,"files":files}
    Path('release/runtime_extraction.json').write_text(json.dumps(summary,indent=2))
    (OUT/'provenance.txt').write_text('Source: official https://dl.google.com/android/repository/sys-img/android/; extracted from system.img / runtime APEX\n')
    if missing: raise SystemExit(4)

if __name__=='__main__':main()
