import ctypes as C
import ctypes.util
from pathlib import Path
import re,json,os,sys,math
os.environ.setdefault('EGL_PLATFORM','surfaceless');os.environ.setdefault('LIBGL_ALWAYS_SOFTWARE','1')
try:
    egl=C.CDLL(ctypes.util.find_library('EGL') or 'libEGL.so.1')
    gl=C.CDLL(ctypes.util.find_library('GLESv2') or 'libGLESv2.so.2')
except OSError as e:
    print(json.dumps({'status':'skipped','reason':str(e)}));sys.exit(0)
P=C.c_void_p;I=C.c_int;U=C.c_uint;B=C.c_ubyte

def fn(lib,name,result,args):
    f=getattr(lib,name);f.restype=result;f.argtypes=args;return f
getproc=fn(egl,'eglGetProcAddress',P,[C.c_char_p])
addr=getproc(b'eglGetPlatformDisplayEXT')
if not addr:print('{"status":"skipped","reason":"No surfaceless EGL platform"}');sys.exit(0)
display=C.CFUNCTYPE(P,U,P,C.POINTER(I))(addr)(0x31DD,None,None)
init=fn(egl,'eglInitialize',U,[P,C.POINTER(I),C.POINTER(I)])
major=I();minor=I()
if not init(display,C.byref(major),C.byref(minor)):
    print('{"status":"skipped","reason":"EGL initialization unavailable"}');sys.exit(0)
fn(egl,'eglBindAPI',U,[U])(0x30A0)
attrs=(I*15)(0x3033,1,0x3040,0x40,0x3024,8,0x3023,8,0x3022,8,0x3021,8,0x3038,0,0)
config=P();count=I()
fn(egl,'eglChooseConfig',U,[P,C.POINTER(I),C.POINTER(P),I,C.POINTER(I)])(display,attrs,C.byref(config),1,C.byref(count))
if not count.value:print('{"status":"skipped","reason":"No ES3 configuration"}');sys.exit(0)
ctxattrs=(I*3)(0x3098,3,0x3038)
context=fn(egl,'eglCreateContext',P,[P,P,P,C.POINTER(I)])(display,config,None,ctxattrs)
surfattrs=(I*5)(0x3057,2,0x3056,2,0x3038)
surface=fn(egl,'eglCreatePbufferSurface',P,[P,P,C.POINTER(I)])(display,config,surfattrs)
if not context or not surface or not fn(egl,'eglMakeCurrent',U,[P,P,P,P])(display,surface,surface,context):
    print('{"status":"skipped","reason":"Cannot make ES3 context current"}');sys.exit(0)
create=fn(gl,'glCreateShader',U,[U]);source=fn(gl,'glShaderSource',None,[U,I,C.POINTER(C.c_char_p),C.POINTER(I)])
compile=fn(gl,'glCompileShader',None,[U]);shaderiv=fn(gl,'glGetShaderiv',None,[U,U,C.POINTER(I)])
logshader=fn(gl,'glGetShaderInfoLog',None,[U,I,C.POINTER(I),C.c_char_p])
text=(Path(__file__).resolve().parents[1]/'payload/jni/real_backdrop/NativeBackdrop.cpp').read_text()
shaders=[]
for name,kind in [('vertex',0x8B31),('fragment',0x8B30)]:
    code=re.search(r'const char\* '+name+r'=R"GLSL\((.*?)\)GLSL";',text,re.S).group(1).encode()
    sh=create(kind);string=C.c_char_p(code);source(sh,1,C.byref(string),None);compile(sh);ok=I();shaderiv(sh,0x8B81,C.byref(ok))
    if not ok.value:
        msg=C.create_string_buffer(8192);logshader(sh,len(msg),None,msg);raise RuntimeError(name+': '+msg.value.decode())
    shaders.append(sh)
program=fn(gl,'glCreateProgram',U,[])()
for sh in shaders:fn(gl,'glAttachShader',None,[U,U])(program,sh)
fn(gl,'glLinkProgram',None,[U])(program);ok=I();fn(gl,'glGetProgramiv',None,[U,U,C.POINTER(I)])(program,0x8B82,C.byref(ok))
assert ok.value,'shader link failed'
gen=fn(gl,'glGenTextures',None,[I,C.POINTER(U)]);bind=fn(gl,'glBindTexture',None,[U,U]);param=fn(gl,'glTexParameteri',None,[U,U,I])
teximage=fn(gl,'glTexImage2D',None,[U,I,I,I,I,I,U,U,P]);textures=(U*2)();gen(2,textures)
pixels=bytes([90,130,190,255,200,100,80,255,40,190,100,255,120,60,210,255]);data=(B*16).from_buffer_copy(pixels)
for i in range(2):
    bind(0x0DE1,textures[i]);param(0x0DE1,0x2801,0x2600);param(0x0DE1,0x2800,0x2600)
    teximage(0x0DE1,0,0x8058,2,2,0,0x1908,0x1401,C.cast(data,P) if i==0 else None)
fbo=U();fn(gl,'glGenFramebuffers',None,[I,C.POINTER(U)])(1,C.byref(fbo))
fn(gl,'glBindFramebuffer',None,[U,U])(0x8D40,fbo.value)
fn(gl,'glFramebufferTexture2D',None,[U,U,U,U,I])(0x8D40,0x8CE0,0x0DE1,textures[1],0)
assert fn(gl,'glCheckFramebufferStatus',U,[U])(0x8D40)==0x8CD5
vao=U();fn(gl,'glGenVertexArrays',None,[I,C.POINTER(U)])(1,C.byref(vao));fn(gl,'glBindVertexArray',None,[U])(vao.value)
fn(gl,'glViewport',None,[I,I,I,I])(0,0,2,2);fn(gl,'glUseProgram',None,[U])(program)
fn(gl,'glActiveTexture',None,[U])(0x84C0);bind(0x0DE1,textures[0])
loc=fn(gl,'glGetUniformLocation',I,[U,C.c_char_p]);uni=fn(gl,'glUniform1i',None,[I,I])
uni(loc(program,b'image'),0)
draw=fn(gl,'glDrawArrays',None,[U,I,I]);read=fn(gl,'glReadPixels',None,[I,I,I,I,U,U,P]);out=(B*16)()
uni(loc(program,b'displayP3'),0);draw(4,0,3);read(0,0,2,2,0x1908,0x1401,C.cast(out,P))
assert max(abs(a-b) for a,b in zip(pixels,out))<=1,'sRGB copy differs'
uni(loc(program,b'displayP3'),1);draw(4,0,3);read(0,0,2,2,0x1908,0x1401,C.cast(out,P))
def lin(x):x=x/255;return x/12.92 if x<=.04045 else ((x+.055)/1.055)**2.4
def enc(x):x=max(0,min(1,x));return round(255*(12.92*x if x<=.0031308 else 1.055*x**(1/2.4)-.055))
expected=[]
for i in range(0,16,4):
    r,g,b=map(lin,pixels[i:i+3]);expected += [enc(1.224940176*r-.224940176*g),enc(-.042056955*r+1.042056955*g),enc(-.019637555*r-.078636046*g+1.098273601*b),255]
assert max(abs(a-b) for a,b in zip(expected,out))<=2,'P3 conversion differs'
assert fn(gl,'glGetError',U,[])()==0,'OpenGL error'
renderer=fn(gl,'glGetString',C.c_char_p,[U])(0x1F01).decode()
print(json.dumps({'status':'passed','renderer':renderer,'tests':['ES3 vertex compile','ES3 fragment compile','link','2x2 sRGB GPU copy','Display-P3 GPU conversion'],'scope':'shader/copy only; no Android HardwareBuffer or display capture on Linux'}))
