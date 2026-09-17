#include "wire.h"
#include <cassert>
#include <cstring>
#include <thread>
#include <unistd.h>
#include <iostream>
int main(){
    using namespace livebg;
    Request q;q.width=1080;q.height=2400;q.outputWidth=540;q.outputHeight=1200;
    assert(Valid(q));
    Request bad=q;bad.magic=0;assert(!Valid(bad));
    bad=q;bad.rotation=4;assert(!Valid(bad));
    bad=q;bad.outputWidth=1081;assert(!Valid(bad));
    bad=q;bad.height=8193;assert(!Valid(bad));
    bad=q;bad.width=-1;assert(!Valid(bad));
    int fds[2];assert(socketpair(AF_UNIX,SOCK_STREAM,0,fds)==0);
    std::thread producer([&]{assert(SendAll(fds[0],&q,sizeof(q)));Reply r;r.generation=12;std::strcpy(r.message,"test");assert(SendAll(fds[0],&r,sizeof(r)));close(fds[0]);});
    Request received;assert(ReceiveAll(fds[1],&received,sizeof(received)));assert(Valid(received));
    Reply reply;assert(ReceiveAll(fds[1],&reply,sizeof(reply)));assert(reply.generation==12);assert(!std::strcmp(reply.message,"test"));
    char byte;assert(!ReceiveAll(fds[1],&byte,1));close(fds[1]);producer.join();
    std::cout<<"PASS: request validation, wire sizes, request/reply transport and EOF\n";
}
