#pragma once
// Private inherited socketpair only. No listener, network port, image files or upload.
#include <cerrno>
#include <cstdint>
#include <sys/socket.h>
#include <time.h>

namespace livebg {
constexpr uint32_t Magic = 0x3142474c; // LGB1, little-endian Android ARM64
constexpr uint32_t Protocol = 1;
struct Request {
    uint32_t magic=Magic, version=Protocol, generation=0;
    int32_t width=0, height=0, rotation=0, outputWidth=0, outputHeight=0;
};
struct Reply {
    uint32_t magic=Magic, version=Protocol, generation=0;
    int32_t width=0, height=0, rotation=0, bufferWidth=0, bufferHeight=0;
    int32_t status=0;
    uint32_t flags=0;
    uint64_t readyNs=0;
    char message[192]{};
};
static_assert(sizeof(Request)==32, "wire request size");
static_assert(sizeof(Reply)==240, "wire reply size");
inline uint64_t NowNs() {
    timespec t{}; clock_gettime(CLOCK_MONOTONIC,&t);
    return uint64_t(t.tv_sec)*1000000000ull+uint64_t(t.tv_nsec);
}
inline bool SendAll(int fd,const void* data,size_t size) {
    const auto* p=static_cast<const char*>(data);
    while(size) {
        const ssize_t n=send(fd,p,size,MSG_NOSIGNAL);
        if(n<0 && errno==EINTR)continue;
        if(n<=0)return false;
        p+=n; size-=size_t(n);
    }
    return true;
}
inline bool ReceiveAll(int fd,void* data,size_t size) {
    auto* p=static_cast<char*>(data);
    while(size) {
        const ssize_t n=recv(fd,p,size,0);
        if(n<0 && errno==EINTR)continue;
        if(n<=0)return false;
        p+=n; size-=size_t(n);
    }
    return true;
}
inline bool Valid(const Request& r) {
    return r.magic==Magic && r.version==Protocol && r.width>0 && r.height>0 &&
        r.width<=8192 && r.height<=8192 && r.outputWidth>0 && r.outputHeight>0 &&
        r.outputWidth<=r.width && r.outputHeight<=r.height && r.rotation>=0 && r.rotation<=3;
}
}
