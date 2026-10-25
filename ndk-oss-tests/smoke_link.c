#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include "cJSON.h"
#include "xxhash.h"
#include "zlib.h"

int main(void) {
    const char *input = "{\"project\":\"ARM64-QEMU\",\"answer\":42,\"active\":true}";
    cJSON *root = cJSON_Parse(input);
    if (!root) { fprintf(stderr,"FAIL cjson: parse\n"); return 11; }
    cJSON *number = cJSON_GetObjectItemCaseSensitive(root,"answer");
    cJSON *project = cJSON_GetObjectItemCaseSensitive(root,"project");
    if (!cJSON_IsNumber(number) || number->valueint != 42 || !cJSON_IsString(project) || strcmp(project->valuestring,"ARM64-QEMU")) {
        fprintf(stderr,"FAIL cjson: fields\n"); cJSON_Delete(root); return 12;
    }
    char *str = cJSON_PrintUnformatted(root);
    if (!str) { cJSON_Delete(root); return 13; }
    printf("CJSON_OK answer=%d serialized_bytes=%zu version=%s\n", number->valueint, strlen(str), cJSON_Version());
    cJSON_free(str); cJSON_Delete(root);
    Bytef compressed[512], recovered[512];
    uLongf compressed_len=sizeof(compressed), recovered_len=sizeof(recovered);
    size_t source_len=strlen(input);
    int rc=compress2(compressed,&compressed_len,(const Bytef *)input,(uLong)source_len,Z_BEST_COMPRESSION);
    if(rc!=Z_OK){fprintf(stderr,"FAIL zlib compress rc=%d\n",rc);return 21;}
    rc=uncompress(recovered,&recovered_len,compressed,compressed_len);
    if(rc!=Z_OK || recovered_len!=source_len || memcmp(recovered,input,source_len)){
        fprintf(stderr,"FAIL zlib uncompress rc=%d\n",rc);return 22;
    }
    printf("ZLIB_OK original=%zu compressed=%lu version=%s\n",source_len,(unsigned long)compressed_len,zlibVersion());
    XXH64_hash_t h64=XXH64(input,source_len,0);
    XXH64_hash_t h3=XXH3_64bits(input,source_len);
    if(!h64 || !h3 || h64==h3){ fprintf(stderr,"FAIL xxhash\n");return 31; }
    printf("XXHASH_OK xxh64=%016llx xxh3=%016llx version=%d\n",(unsigned long long)h64,(unsigned long long)h3,XXH_versionNumber());
    puts("ALL_LINKED_TESTS_PASS");
    return 0;
}
