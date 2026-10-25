#define _GNU_SOURCE
#include <stdio.h>
#include <dlfcn.h>
#include <stdint.h>
#include <string.h>

struct libdef {const char *name; const char *symbol;};
int main(void){
    struct libdef libs[]={{"liboss_cjson.so","cJSON_Version"}, {"liboss_zlib.so","zlibVersion"}, {"liboss_xxhash.so","XXH_versionNumber"}};
    for(unsigned i=0;i<3;i++){
        void *h=dlopen(libs[i].name,RTLD_NOW|RTLD_LOCAL);
        if(!h){fprintf(stderr,"DLOPEN_FAIL %s %s\n",libs[i].name,dlerror());return 40+(int)i;}
        dlerror();void *symbol=dlsym(h,libs[i].symbol);
        const char *e=dlerror();
        if(e || !symbol){fprintf(stderr,"DLSYM_FAIL %s %s\n",libs[i].name,e?e:"NULL");return 50+(int)i;}
        if(i==2){int (*v)(void)=(int(*)(void))symbol;printf("DLOPEN_OK %s %s=%d\n",libs[i].name,libs[i].symbol,v());}
        else{const char *(*v)(void)=(const char*(*)(void))symbol;const char *value=v();if(!value){return 60+(int)i;}printf("DLOPEN_OK %s %s=%s\n",libs[i].name,libs[i].symbol,value);}
        dlclose(h);
    }
    puts("ALL_DLOPEN_TESTS_PASS");return 0;
}
