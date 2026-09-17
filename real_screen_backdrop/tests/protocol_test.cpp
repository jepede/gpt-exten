#include "Protocol.h"
#include <cassert>
#include <cstring>
#include <thread>
#include <iostream>
using namespace screenbackdrop::wire;
int main(){
    Request q;q.sequence=17;assert(Valid(q));
    q.maxEdge=0;assert(!Valid(q));q.maxEdge=1280;q.magic=0;assert(!Valid(q));
    Response r;r.sequence=17;r.width=720;r.height=1280;r.screenWidth=1080;r.screenHeight=1920;
    r.timestampNs=NowNs();assert(Valid(r,17));assert(!Valid(r,18));
    r.rotation=4;assert(!Valid(r,17));r.rotation=0;
    r.width=0;assert(!Valid(r,17));r.width=720;
    r.colorSpace=16;assert(!Valid(r,17));r.colorSpace=7;assert(Valid(r,17));
    r.screenHeight=999999;assert(!Valid(r,17));r.screenHeight=1920;
    int sockets[2];assert(socketpair(AF_UNIX,SOCK_STREAM,0,sockets)==0);
    std::thread producer([&]{const auto* p=reinterpret_cast<const char*>(&r);for(size_t i=0;i<sizeof(r);i+=3){size_t n=std::min(size_t(3),sizeof(r)-i);assert(Write(sockets[0],p+i,n));}close(sockets[0]);});
    Response received;assert(Read(sockets[1],&received,sizeof(received)));assert(std::memcmp(&r,&received,sizeof(r))==0);
    char byte;assert(!Read(sockets[1],&byte,1));close(sockets[1]);producer.join();
    std::cout<<"PASS: request validation, frame validation, sequence, size, rotation, colorspace, fragmented stream, EOF\n";
}
