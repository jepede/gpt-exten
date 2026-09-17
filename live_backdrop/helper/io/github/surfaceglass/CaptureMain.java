package io.github.surfaceglass;

import android.hardware.HardwareBuffer;
import android.os.Build;
import android.os.IBinder;
import java.lang.reflect.Constructor;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;

/**
 * Launched only by the visible host's opt-in control, using its existing root UID.
 * ScreenCapture remains subject to system permission checks. No hidden-API
 * exemptions, secure-content capture, recording, files, network, or APK service.
 * The platform ScreenCapture JNI waits its producer fence before delivering the
 * HardwareBuffer on the Android 16 release implementation used as the reference.
 */
public final class CaptureMain {
    private static native boolean bootstrap(int expectedParent);
    private static native int[] next(int fd);
    private static native boolean deliver(int fd, int[] request, HardwareBuffer buffer,
                                          int flags, int error, String message);
    private static String describe(Throwable t) {
        if (t instanceof InvocationTargetException && t.getCause()!=null) t=t.getCause();
        return t.getClass().getSimpleName()+": "+String.valueOf(t.getMessage());
    }
    public static void main(String[] args) {
        if (args.length!=3) { System.err.println("SurfaceGlass: fd, JNI path, parent pid required"); return; }
        try {
            if (Build.VERSION.SDK_INT<34 || Build.VERSION.SDK_INT>36)
                throw new IllegalStateException("Capture helper requires Android API 34..36; this ROM is not enabled");
            if (android.os.Process.myUid()!=0)
                throw new SecurityException("Capture helper requires the host's existing root UID");
            final int fd=Integer.parseInt(args[0]);
            System.load(args[1]);
            if (!bootstrap(Integer.parseInt(args[2]))) return;
            run(fd);
        } catch (Throwable error) {
            System.err.println("SurfaceGlass capture helper stopped: "+describe(error));
        }
    }
    private static void run(int fd) {
        try {
            final Class<?> surfaceControl=Class.forName("android.view.SurfaceControl");
            final Method idsMethod=surfaceControl.getMethod("getPhysicalDisplayIds");
            final Method tokenMethod=surfaceControl.getMethod("getPhysicalDisplayToken",long.class);
            final Class<?> capture=Class.forName("android.window.ScreenCapture");
            final Class<?> argsClass=Class.forName("android.window.ScreenCapture$DisplayCaptureArgs");
            final Class<?> builderClass=Class.forName("android.window.ScreenCapture$DisplayCaptureArgs$Builder");
            final Constructor<?> constructor=builderClass.getConstructor(IBinder.class);
            final Method setSize=builderClass.getMethod("setSize",int.class,int.class);
            final Method setPixelFormat=builderClass.getMethod("setPixelFormat",int.class);
            final Method setSecure=builderClass.getMethod("setCaptureSecureLayers",boolean.class);
            final Method setProtected=builderClass.getMethod("setAllowProtected",boolean.class);
            final Method build=builderClass.getMethod("build");
            final Method captureDisplay=capture.getMethod("captureDisplay",argsClass);
            Method seamless=null;
            try { seamless=builderClass.getMethod("setHintForSeamlessTransition",boolean.class); }
            catch (NoSuchMethodException ignored) { /* Older release: safe default is false. */ }
            while (true) {
                final int[] request=next(fd);
                if (request==null) return;
                HardwareBuffer buffer=null;
                try {
                    final long[] ids=(long[])idsMethod.invoke(null);
                    if (ids==null || ids.length==0) throw new IllegalStateException("No physical display");
                    final IBinder token=(IBinder)tokenMethod.invoke(null,ids[0]);
                    if (token==null) throw new IllegalStateException("Null physical display token");
                    final Object builder=constructor.newInstance(token);
                    setSize.invoke(builder,request[4],request[5]);
                    setPixelFormat.invoke(builder,1); // PixelFormat.RGBA_8888
                    setSecure.invoke(builder,false);
                    setProtected.invoke(builder,false);
                    // App-local lens usage, not an exported HDR screenshot. On the
                    // reference platform this avoids an additional gain-map capture.
                    if (seamless!=null) seamless.invoke(builder,true);
                    final Object result=captureDisplay.invoke(null,build.invoke(builder));
                    if (result==null) throw new IllegalStateException("ScreenCapture returned null (permission, timeout or ROM incompatibility)");
                    final Class<?> resultClass=result.getClass();
                    buffer=(HardwareBuffer)resultClass.getMethod("getHardwareBuffer").invoke(result);
                    final boolean secure=(Boolean)resultClass.getMethod("containsSecureLayers").invoke(result);
                    final boolean hdr=(Boolean)resultClass.getMethod("containsHdrLayers").invoke(result);
                    if (secure) throw new SecurityException("Refusing a buffer reporting secure layers");
                    if (buffer==null) throw new IllegalStateException("No HardwareBuffer returned");
                    if (!deliver(fd,request,buffer,hdr?1:0,0,"")) return;
                } catch (Throwable error) {
                    final String message=describe(error);
                    System.err.println("SurfaceGlass capture: "+message);
                    if (!deliver(fd,request,null,0,-1,message)) return;
                    // Fail closed. A user may explicitly retry after fixing the cause.
                    return;
                } finally {
                    if (buffer!=null) buffer.close();
                }
            }
        } catch (Throwable error) {
            final int[] request=next(fd);
            if (request!=null) deliver(fd,request,null,0,-1,describe(error));
            System.err.println("SurfaceGlass API discovery: "+describe(error));
        }
    }
}
