package com.ytbl.capture;

import java.lang.reflect.Method;
import java.util.Arrays;

/** Minimal ART host. The native ImGui entry is unchanged apart from its symbol
 * name. Keeping capture and SurfaceControls in this process avoids sending
 * meaningless raw pointers to a separate app_process.
 */
public final class HostMain {
    private static native int nativeRun(String[] argv);
    private HostMain() {}
    public static void main(String[] args) {
        int status=1;
        try {
            if(args.length<2)throw new IllegalArgumentException("Use the packaged imgui_chain_1_47 launcher");
            Class<?> looper=Class.forName("android.os.Looper");
            Method main=looper.getMethod("getMainLooper");
            if(main.invoke(null)==null)looper.getMethod("prepareMainLooper").invoke(null);
            System.load(args[0]);
            status=nativeRun(Arrays.copyOfRange(args,1,args.length));
        }catch(Throwable error){
            System.err.println("[YtblExclude] Host startup failed:");error.printStackTrace(System.err);
        }finally{
            // The native UI returning is terminal for this command, not a service.
            System.exit(status);
        }
    }
}
