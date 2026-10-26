#include <EGL/egl.h>
#include <GLES3/gl3.h>
#include <dlfcn.h>
#include <stdio.h>
#include <string.h>
#include <sys/system_properties.h>

int main(void) {
    setbuf(stdout, NULL);
    char release[PROP_VALUE_MAX] = {0};
    char sdk[PROP_VALUE_MAX] = {0};
    __system_property_get("ro.build.version.release", release);
    __system_property_get("ro.build.version.sdk", sdk);
    printf("[ENV] Android release=%s sdk=%s\n", release, sdk);
    const char *libraries[] = {"libgui.so", "libutils.so", "libandroid.so", "libEGL.so",
                               "libGLESv3.so", "libvulkan.so", "libbinder_ndk.so"};
    for (unsigned i = 0; i < sizeof(libraries) / sizeof(libraries[0]); ++i) {
        void *handle = dlopen(libraries[i], RTLD_NOW | RTLD_LOCAL);
        printf("[ENV] dlopen %s=%s\n", libraries[i], handle ? "OK" : dlerror());
    }
    EGLDisplay display = eglGetDisplay(EGL_DEFAULT_DISPLAY);
    EGLint major = 0, minor = 0;
    EGLBoolean initialized = eglInitialize(display, &major, &minor);
    printf("[EGL] initialized=%u version=%d.%d vendor=%s\n", initialized, major, minor,
           initialized ? eglQueryString(display, EGL_VENDOR) : "unavailable");
    if (!initialized) return 10;
    EGLint count = 0;
    EGLConfig config = NULL;
    EGLint attributes[] = {EGL_SURFACE_TYPE, EGL_PBUFFER_BIT, EGL_RENDERABLE_TYPE,
                           EGL_OPENGL_ES3_BIT, EGL_RED_SIZE, 8, EGL_GREEN_SIZE, 8,
                           EGL_BLUE_SIZE, 8, EGL_ALPHA_SIZE, 8, EGL_NONE};
    if (!eglChooseConfig(display, attributes, &config, 1, &count) || count < 1) {
        printf("[EGL] pbuffer configuration unavailable error=0x%x\n", eglGetError());
        return 11;
    }
    EGLint context_attributes[] = {EGL_CONTEXT_CLIENT_VERSION, 3, EGL_NONE};
    EGLContext context = eglCreateContext(display, config, EGL_NO_CONTEXT, context_attributes);
    EGLint surface_attributes[] = {EGL_WIDTH, 4, EGL_HEIGHT, 4, EGL_NONE};
    EGLSurface surface = eglCreatePbufferSurface(display, config, surface_attributes);
    EGLBoolean current = eglMakeCurrent(display, surface, surface, context);
    printf("[EGL] context=%p pbuffer=%p current=%u error=0x%x\n", context, surface,
           current, eglGetError());
    if (!context || !surface || !current) return 12;
    printf("[GL] vendor=%s renderer=%s version=%s\n", glGetString(GL_VENDOR),
           glGetString(GL_RENDERER), glGetString(GL_VERSION));
    void *gles = dlopen("libGLESv3.so", RTLD_NOW | RTLD_LOCAL);
    typedef void (*read_pixels_fn)(GLint, GLint, GLsizei, GLsizei, GLenum, GLenum, void *);
    read_pixels_fn read_pixels = (read_pixels_fn)dlsym(gles, "glReadPixels");
    printf("[GL] glReadPixels=%s\n", read_pixels ? "available" : "MISSING");
    if (!read_pixels) return 13;
    unsigned char pixels[4 * 4 * 4];
    memset(pixels, 0xcd, sizeof(pixels));
    glViewport(0, 0, 4, 4);
    glClearColor(0.25f, 0.5f, 0.75f, 1.0f);
    glClear(GL_COLOR_BUFFER_BIT);
    glFinish();
    read_pixels(0, 0, 4, 4, GL_RGBA, GL_UNSIGNED_BYTE, pixels);
    unsigned changed = 0;
    for (unsigned i = 0; i < sizeof(pixels); ++i) changed += pixels[i] != 0xcd;
    printf("[PIXELS] first=%u,%u,%u,%u changed_bytes=%u gl_error=0x%x\n",
           pixels[0], pixels[1], pixels[2], pixels[3], changed, glGetError());
    int match = pixels[0] >= 62 && pixels[0] <= 66 && pixels[1] >= 126 &&
                pixels[1] <= 130 && pixels[2] >= 189 && pixels[2] <= 193 && pixels[3] == 255;
    printf("[PIXELS] clear_color_readback=%s\n", match ? "PASS" : "FAIL");
    eglMakeCurrent(display, EGL_NO_SURFACE, EGL_NO_SURFACE, EGL_NO_CONTEXT);
    eglDestroySurface(display, surface);
    eglDestroyContext(display, context);
    eglTerminate(display);
    return match ? 0 : 14;
}
