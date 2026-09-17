#include <cerrno>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <limits.h>
#include <string>
#include <vector>
#include <sys/stat.h>
#include <unistd.h>

int main(int argc,char** argv) {
    if(getuid()!=0 || geteuid()!=0){std::fprintf(stderr,"Owner-root launch required; no elevation is performed.\n");return 1;}
    char path[PATH_MAX];ssize_t n=readlink("/proc/self/exe",path,sizeof(path)-1);
    if(n<=0 || n>=static_cast<ssize_t>(sizeof(path)-1)){std::perror("readlink self");return 1;}path[n]=0;
    std::string exe=path;auto slash=exe.rfind('/');
    if(slash==std::string::npos)return 1;
    std::string runtime=exe.substr(0,slash)+"/capture_runtime";
    if(const char* overrideDir=std::getenv("YTBL_CAPTURE_DIR"))if(*overrideDir)runtime=overrideDir;
    char canonical[PATH_MAX];
    if(!realpath(runtime.c_str(),canonical)){std::perror("capture_runtime");return 1;}runtime=canonical;
    std::string dex=runtime+"/capture.dex.jar", host=runtime+"/libytbl_host.so";
    for(const auto& file:{dex,host}){
        struct stat st{};
        if(stat(file.c_str(),&st) || !S_ISREG(st.st_mode) || access(file.c_str(),R_OK)){
            std::fprintf(stderr,"Missing runtime file: %s\n",file.c_str());return 1;
        }
        if(st.st_mode & (S_IWGRP|S_IWOTH)){
            std::fprintf(stderr,"Refusing group/world-writable runtime file: %s\n",file.c_str());return 1;
        }
    }
    struct stat ds{};stat(dex.c_str(),&ds);
    if(ds.st_mode & S_IWUSR){std::fprintf(stderr,"Set capture.dex.jar read-only (chmod 444) before launch.\n");return 1;}
    if(setenv("CLASSPATH",dex.c_str(),1)){std::perror("CLASSPATH");return 1;}
    unsetenv("LD_PRELOAD");unsetenv("LD_LIBRARY_PATH");
    std::vector<std::string> args={"/system/bin/app_process","/system/bin","--nice-name=imgui_chain_1_47",
                                  "com.ytbl.capture.HostMain",host,exe};
    for(int i=1;i<argc;++i)args.emplace_back(argv[i]);
    std::vector<char*> values;for(auto& a:args)values.push_back(a.data());values.push_back(nullptr);
    execv(values[0],values.data());std::perror("app_process");return 127;
}
