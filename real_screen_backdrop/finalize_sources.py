from pathlib import Path
root=Path(__file__).resolve().parent

def replace(path,old,new):
    text=path.read_text()
    if new in text:return
    if text.count(old)!=1:raise RuntimeError('Unexpected source anchor: '+str(path))
    path.write_text(text.replace(old,new))

# Invoke the public superclass declaration, not a method declared on the
# package-private anonymous listener returned by AOSP's factory.
replace(root/'payload/capture/Main.java',
        'Object result=get(listener,"getBuffer");',
        'Object result=Class.forName("android.window.ScreenCapture$SynchronousScreenCaptureListener")\n'
        '                    .getMethod("getBuffer").invoke(listener);')
# A context may have been recreated during a Surface rebind. Never poll syncs
# from a previous context before noticing that transition.
replace(root/'payload/jni/real_backdrop/NativeBackdrop.cpp',
        'void UpdateTexture() {\n    if(s.stop.load())return;',
        'void UpdateTexture() {\n    if(s.stop.load())return;\n'
        '    if(eglGetCurrentContext()==EGL_NO_CONTEXT){Status("No current GLES context");return;}\n'
        '    if(s.context!=EGL_NO_CONTEXT && s.context!=eglGetCurrentContext())DropGL(true);')
# Termux's LD_PRELOAD can interfere with the system app_process loader. Filter
# only in the spawned child's private environment, not in the user shell.
replace(root/'payload/jni/real_backdrop/NativeBackdrop.cpp',
        'if(std::strncmp(*p,"CLASSPATH=",10)!=0)envStrings.emplace_back(*p);',
        'if(std::strncmp(*p,"CLASSPATH=",10)!=0 && std::strncmp(*p,"LD_PRELOAD=",11)!=0 &&\n'
        '        std::strncmp(*p,"LD_LIBRARY_PATH=",16)!=0)envStrings.emplace_back(*p);')
# Inserting a dependency before the host's IMGUI_DEFINE_MATH_OPERATORS can
# change ImGui inline declarations. Insert after the existing Ytbl include.
replace(root/'install.py',
        '        text=\'#include "SurfaceBackdropUi.h"\\n\'+text',
        '''        host_include = '#include "ytbl.h"'
        if host_include in text:
            text=one(text,host_include,host_include+'\\n#include "SurfaceBackdropUi.h"','Ytbl include order')
        else:
            text=('#ifndef IMGUI_DEFINE_MATH_OPERATORS\\n#define IMGUI_DEFINE_MATH_OPERATORS\\n#endif\\n'
                  '#include "SurfaceBackdropUi.h"\\n')+text''')
# An app_process helper must not stay alive on Binder/runtime threads after
# its parent closes the sole local connection.
replace(root/'payload/capture/Main.java',
        '            System.err.println("[YtblCapture] stopped: "+cause(error));\n        }\n    }\n}',
        '            System.err.println("[YtblCapture] stopped: "+cause(error));\n        }\n'
        '        System.exit(0); // End only this child; never a persistent capture service.\n    }\n}')
replace(root/'payload/jni/real_backdrop/SurfaceBackdropUi.h',
        'ImGui::Button("停止并重新连接")',
        'ImGui::Button("停止采集（重新勾选以重连）")')
