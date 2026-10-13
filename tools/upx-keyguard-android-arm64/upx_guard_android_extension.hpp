// UPX-KeyGuard: host packer for Android AArch64 executable payloads.
// SPDX-License-Identifier: GPL-2.0-or-later
// This is a UPX-source extension with zlib compression and AES-256-GCM
// authenticated encryption, not the stock UPX Android runtime stub.
#ifndef UPX_GUARD_ANDROID_EXTENSION_HPP
#define UPX_GUARD_ANDROID_EXTENSION_HPP
#if defined(__linux__) && defined(__x86_64__)
#include <zlib.h>
namespace upx_keyguard {

static bool is_android_arm64_pie(const char *name) {
    int fd = open(name, O_RDONLY | O_CLOEXEC | O_NOFOLLOW);
    if (fd < 0) return false;
    unsigned char e[64]={0};
    bool ok = read_n(fd, e, sizeof(e)); close(fd);
    return ok && !memcmp(e, "\177ELF", 4) && e[4] == 2 && e[5] == 1 &&
           e[18] == 183 && e[19] == 0 &&
           (e[16] == 2 || e[16] == 3);
}
static int seal_android(int argc, char **argv) {
    std::string key_file, stub_file, output, source;
    for (int i = 2; i < argc; ++i) {
        if (!strcmp(argv[i], "--key-file") && i+1 < argc) key_file = argv[++i];
        else if (!strcmp(argv[i], "--stub") && i+1 < argc) stub_file = argv[++i];
        else if ((!strcmp(argv[i], "-o") || !strcmp(argv[i], "--output")) &&
                 i+1 < argc) output = argv[++i];
        else if (argv[i][0]=='-') return fail("unknown --seal-android-arm64 option");
        else if (source.empty()) source=argv[i];
        else return fail("one input required");
    }
    if (key_file.empty() || stub_file.empty() || output.empty() || source.empty())
        return fail("usage: upx --seal-android-arm64 --key-file KEY --stub LOADER -o OUT INPUT");
    if (output==source || output==stub_file || output==key_file)
        return fail("input and output paths must differ");
    if (!is_android_arm64_pie(source.c_str()) ||
        !is_android_arm64_pie(stub_file.c_str()))
        return fail("source and loader must both be Android-compatible ARM64 ELF64");
    unsigned char key[32]={0};
    if (!key_from_file(key_file.c_str(),key))
        return fail("key must be an external file containing exactly 32 bytes");
    int input=open(source.c_str(),O_RDONLY|O_CLOEXEC|O_NOFOLLOW);
    int stub=open(stub_file.c_str(),O_RDONLY|O_CLOEXEC|O_NOFOLLOW);
    std::string output_tmp=output+".keyguard-tmp-XXXXXX";
    int target=mkstemp(output_tmp.data());
    if (input<0 || stub<0 || target<0) {
        if(input>=0)close(input);
        if(stub>=0)close(stub);
        if(target>=0){close(target);unlink(output_tmp.c_str());}
        OPENSSL_cleanse(key,sizeof(key));
        return fail("cannot open input, loader or output");
    }
    EVP_CIPHER_CTX *ctx=EVP_CIPHER_CTX_new();
    z_stream z={};
    bool initialized=false,ok=ctx!=nullptr;
    unsigned char nonce[12]={},tag[16]={};
    unsigned char raw[kChunk],packed[kChunk],cipher[kChunk+32],footer[44]={};
    uint64_t ciphertext_length=0, uncompressed_length=0;
    int encrypted_len=0,last_encrypted=0;
    if(ok)ok=RAND_bytes(nonce,sizeof(nonce))==1;
    if(ok)ok=copy_fd(stub,target);
    if(ok)ok=EVP_EncryptInit_ex(ctx,EVP_aes_256_gcm(),nullptr,nullptr,nullptr)==1 &&
               EVP_CIPHER_CTX_ctrl(ctx,EVP_CTRL_GCM_SET_IVLEN,12,nullptr)==1 &&
               EVP_EncryptInit_ex(ctx,nullptr,nullptr,key,nonce)==1 &&
               EVP_EncryptUpdate(ctx,nullptr,&encrypted_len,kAAD,sizeof(kAAD)-1)==1;
    OPENSSL_cleanse(key,sizeof(key));
    if(ok){ok=deflateInit(&z,Z_BEST_COMPRESSION)==Z_OK;initialized=ok;}
    bool eof=false,finished=false;
    while(ok && !finished) {
        if(z.avail_in==0 && !eof){
            ssize_t count=read(input,raw,sizeof(raw));
            if(count<0 && errno==EINTR)continue;
            if(count<0){ok=false;break;}
            if(count==0)eof=true;
            else {z.next_in=raw;z.avail_in=(uInt)count;uncompressed_length+=(size_t)count;}
        }
        z.next_out=packed;z.avail_out=(uInt)sizeof(packed);
        uInt before=z.avail_in;
        int result=deflate(&z,eof?Z_FINISH:Z_NO_FLUSH);
        size_t compressed_length=sizeof(packed)-z.avail_out;
        if(result!=Z_OK && result!=Z_STREAM_END) {ok=false;break;}
        if(compressed_length) {
            if(EVP_EncryptUpdate(ctx,cipher,&encrypted_len,packed,(int)compressed_length)!=1 ||
               encrypted_len<0 || !write_n(target,cipher,(size_t)encrypted_len)){
                ok=false;break;
            }
            ciphertext_length+=(size_t)encrypted_len;
        }
        if(result==Z_STREAM_END)finished=true;
        else if(before==z.avail_in && compressed_length==0){ok=false;break;}
    }
    if(initialized)deflateEnd(&z);
    if(ok && finished)ok=EVP_EncryptFinal_ex(ctx,cipher,&last_encrypted)==1;
    if(ok && last_encrypted){
        ok=write_n(target,cipher,(size_t)last_encrypted);
        ciphertext_length+=(size_t)last_encrypted;
    }
    if(ok)ok=EVP_CIPHER_CTX_ctrl(ctx,EVP_CTRL_GCM_GET_TAG,16,tag)==1;
    if(ok){
        memcpy(footer,kMagic,8);
        put_le64(footer+8,ciphertext_length);
        memcpy(footer+16,nonce,12);memcpy(footer+28,tag,16);
        ok=write_n(target,footer,sizeof(footer));
    }
    if(ctx)EVP_CIPHER_CTX_free(ctx);
    OPENSSL_cleanse(raw,sizeof(raw));
    OPENSSL_cleanse(packed,sizeof(packed));
    OPENSSL_cleanse(cipher,sizeof(cipher));
    close(input);close(stub);
    if(fchmod(target,0755)!=0)ok=false;
    if(fsync(target)!=0)ok=false;
    if(close(target)!=0)ok=false;
    if(ok && rename(output_tmp.c_str(),output.c_str())!=0)ok=false;
    if(!ok){
        unlink(output_tmp.c_str());
        return fail("Android ARM64 compress-and-seal failed");
    }
    std::printf("UPX-KeyGuard Android ARM64: compressed+encrypted %llu -> %llu bytes: %s\n",
                (unsigned long long)uncompressed_length,
                (unsigned long long)ciphertext_length,output.c_str());
    return 0;
}
} // namespace upx_keyguard
#endif
#endif
