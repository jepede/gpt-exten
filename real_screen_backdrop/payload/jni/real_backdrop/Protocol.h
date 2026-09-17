#pragma once
#include <cstdint>
#include <cerrno>
#include <cstddef>
#include <sys/socket.h>
#include <unistd.h>
#include <time.h>

namespace screenbackdrop::wire {
constexpr uint32_t Magic = 0x59474231u; // YGB1, versioned local socketpair protocol
constexpr uint32_t Version = 1;
struct Request { uint32_t magic=Magic, version=Version, sequence=0, maxEdge=1280; };
struct Response {
    uint32_t magic=Magic, version=Version, sequence=0;
    int32_t status=0;
    uint32_t width=0, height=0, screenWidth=0, screenHeight=0, rotation=0, colorSpace=0;
    uint64_t timestampNs=0;
    char message[192]{};
};
static_assert(sizeof(Request)==16);
static_assert(sizeof(Response)==240);
inline uint64_t NowNs() {
    timespec ts{};
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return uint64_t(ts.tv_sec)*1000000000ull + uint64_t(ts.tv_nsec);
}
inline bool Valid(const Request& q) {
    return q.magic==Magic && q.version==Version && q.maxEdge>=320 && q.maxEdge<=2560;
}
inline bool Valid(const Response& r, uint32_t sequence) {
    if(r.magic!=Magic || r.version!=Version || r.sequence!=sequence) return false;
    if(r.status) return true;
    return r.width>0 && r.height>0 && r.width<=4096 && r.height<=4096 &&
           uint64_t(r.width)*r.height<=16777216 &&
           r.screenWidth>0 && r.screenHeight>0 && r.screenWidth<=16384 &&
           r.screenHeight<=16384 && r.rotation<4 && (r.colorSpace==0 || r.colorSpace==7);
}
inline bool Read(int fd, void* data, size_t size) {
    auto* p=static_cast<unsigned char*>(data);
    while(size) {
        const ssize_t n=recv(fd,p,size,0);
        if(n<0 && errno==EINTR) continue;
        if(n<=0) return false;
        p+=n; size-=static_cast<size_t>(n);
    }
    return true;
}
inline bool Write(int fd, const void* data, size_t size) {
    auto* p=static_cast<const unsigned char*>(data);
    while(size) {
        const ssize_t n=send(fd,p,size,MSG_NOSIGNAL);
        if(n<0 && errno==EINTR) continue;
        if(n<=0) return false;
        p+=n; size-=static_cast<size_t>(n);
    }
    return true;
}
} // namespace screenbackdrop::wire
