package com.ytbl.capture;

import java.lang.reflect.Constructor;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;

/**
 * Local, opt-in visual backdrop for the owner's rooted device.
 * Runs only as a child of the visible native UI. No files, sockets exposed to
 * other apps, recording, networking, permission changes, or protected capture.
 * Platform API references: AOSP android16-release ScreenCapture.java and
 * android_window_ScreenCapture.cpp. DisplayControl's system classloader loading
 * pattern is also used by Genymobile scrcpy (Apache-2.0); see SOURCES.md.
 */
public final class Main {
    private static native boolean nativeInit(int fd);
    private static native int[] nativeNext(int fd);
    private static native boolean nativeFrame(int fd, int sequence, Object buffer,
                                              int screenWidth, int screenHeight,
                                              int rotation, int colorSpace);
    private static native boolean nativeError(int fd, int sequence, int status, String message);
    private Main() {}

    private static Object call(Object target, String name, Class<?>[] types, Object... args) throws Exception {
        Class<?> cls = target instanceof Class<?> ? (Class<?>) target : target.getClass();
        Method method = cls.getMethod(name, types);
        return method.invoke(target instanceof Class<?> ? null : target, args);
    }
    private static Object get(Object target, String name) throws Exception {
        return call(target,name,new Class<?>[0]);
    }
    private static int fieldInt(Object object, String name) throws Exception {
        return object.getClass().getField(name).getInt(object);
    }
    private static String cause(Throwable error) {
        while(error instanceof InvocationTargetException && error.getCause()!=null) error=error.getCause();
        return error.getClass().getSimpleName()+": "+String.valueOf(error.getMessage());
    }
    private static void closeBuffer(Object buffer) {
        if(buffer!=null) try { get(buffer,"close"); } catch(Exception ignored) {}
    }
    private static final class Info {
        int width,height,rotation; String unique;
        Info(Object info) throws Exception {
            if(info==null) throw new IllegalStateException("Display 0 is unavailable");
            width=fieldInt(info,"logicalWidth"); height=fieldInt(info,"logicalHeight");
            rotation=fieldInt(info,"rotation");
            unique=String.valueOf(info.getClass().getField("uniqueId").get(info));
            if(width<1 || height<1 || width>16384 || height>16384 || rotation<0 || rotation>3)
                throw new IllegalStateException("Invalid display geometry");
        }
        boolean same(Info other) {
            return width==other.width && height==other.height && rotation==other.rotation && unique.equals(other.unique);
        }
    }
    private static final class Capture {
        final Object displayManager;
        final Class<?> control,capture,argsClass;
        final Constructor<?> builder;
        final Method captureMethod,makeListener;
        Object displayToken;
        String displayUnique="";
        Capture() throws Exception {
            Class<?> version=Class.forName("android.os.Build$VERSION");
            int sdk=version.getField("SDK_INT").getInt(null);
            if(sdk<34 || sdk>36) throw new UnsupportedOperationException("This helper targets Android 14-16 (SDK 34-36), got "+sdk);
            Class<?> looper=Class.forName("android.os.Looper");
            if(get(looper,"getMainLooper")==null) get(looper,"prepareMainLooper");
            displayManager=get(Class.forName("android.hardware.display.DisplayManagerGlobal"),"getInstance");
            Class<?> found=Class.forName("android.view.SurfaceControl");
            try { found.getMethod("getPhysicalDisplayToken",long.class); }
            catch(NoSuchMethodException e) {
                String cp=System.getenv("SYSTEMSERVERCLASSPATH");
                if(cp==null || cp.isEmpty()) cp="/system/framework/services.jar";
                Class<?> factory=Class.forName("com.android.internal.os.ClassLoaderFactory");
                Method make=factory.getDeclaredMethod("createClassLoader",String.class,String.class,String.class,
                                                     ClassLoader.class,int.class,boolean.class,String.class);
                ClassLoader loader=(ClassLoader)make.invoke(null,cp,null,null,ClassLoader.getSystemClassLoader(),0,true,null);
                found=loader.loadClass("com.android.server.display.DisplayControl");
                Method load=Runtime.class.getDeclaredMethod("loadLibrary0",Class.class,String.class);
                load.setAccessible(true);
                load.invoke(Runtime.getRuntime(),found,"android_servers");
            }
            control=found;
            capture=Class.forName("android.window.ScreenCapture");
            argsClass=Class.forName("android.window.ScreenCapture$DisplayCaptureArgs");
            builder=Class.forName("android.window.ScreenCapture$DisplayCaptureArgs$Builder")
                         .getConstructor(Class.forName("android.os.IBinder"));
            makeListener=capture.getMethod("createSyncCaptureListener");
            captureMethod=capture.getMethod("captureDisplay",argsClass,
                                  Class.forName("android.window.ScreenCapture$ScreenCaptureListener"));
        }
        Info info() throws Exception {
            return new Info(call(displayManager,"getDisplayInfo",new Class<?>[]{int.class},0));
        }
        Object token(Info info) throws Exception {
            if(displayToken!=null && displayUnique.equals(info.unique)) return displayToken;
            long[] ids=(long[])get(control,"getPhysicalDisplayIds");
            if(ids==null || ids.length==0) throw new IllegalStateException("No physical display");
            long id=ids[0];
            if(info.unique.startsWith("local:")) {
                long required=Long.parseLong(info.unique.substring(6)); boolean matched=false;
                for(long candidate:ids) if(candidate==required) {id=candidate;matched=true;break;}
                if(!matched) throw new IllegalStateException("Display 0 does not match a physical display token");
            } else if(ids.length!=1) throw new IllegalStateException("Ambiguous non-physical default display");
            displayToken=call(control,"getPhysicalDisplayToken",new Class<?>[]{long.class},id);
            if(displayToken==null) throw new SecurityException("No display token; system permission denied");
            displayUnique=info.unique;
            return displayToken;
        }
        Object frame(Info info,int maxEdge) throws Exception {
            Object b=builder.newInstance(token(info));
            float scale=Math.min(1.0f,(float)maxEdge/Math.max(info.width,info.height));
            int width=Math.max(1,Math.round(info.width*scale));
            int height=Math.max(1,Math.round(info.height*scale));
            call(b,"setSize",new Class<?>[]{int.class,int.class},width,height);
            call(b,"setPixelFormat",new Class<?>[]{int.class},1); // RGBA_8888
            call(b,"setCaptureSecureLayers",new Class<?>[]{boolean.class},false);
            call(b,"setAllowProtected",new Class<?>[]{boolean.class},false);
            Object args=get(b,"build");
            Object listener=makeListener.invoke(null);
            int status=(Integer)captureMethod.invoke(null,args,listener);
            if(status!=0) throw new SecurityException("captureDisplay status="+status+"; no permission bypass attempted");
            Object result=get(listener,"getBuffer");
            if(result==null) throw new IllegalStateException("Capture callback failed or timed out");
            return result;
        }
    }
    public static void main(String[] args) {
        if(args.length!=2 || !"3".equals(args[0])) {
            System.err.println("Run only through the visible Ytbl screen-background control."); return;
        }
        int fd=3;
        try {
            System.load(args[1]);
            if(!nativeInit(fd)) throw new SecurityException("Owner-root socketpair session required");
            Capture capture=null;
            System.err.println("[YtblCapture] Local screen background active; secure/protected capture is OFF.");
            for(;;) {
                int[] request=nativeNext(fd);
                if(request==null) break;
                Object hardware=null, result=null;
                try {
                    if(capture==null) capture=new Capture();
                    Info before=capture.info();
                    result=capture.frame(before,request[1]);
                    hardware=get(result,"getHardwareBuffer");
                    if(Boolean.TRUE.equals(get(result,"containsSecureLayers")))
                        throw new SecurityException("Refusing a buffer containing secure layers");
                    if(Boolean.TRUE.equals(get(result,"containsHdrLayers")))
                        throw new UnsupportedOperationException("HDR capture requires a separate color-managed path");
                    Object color=get(result,"getColorSpace");
                    int colorId=color==null ? 0 : (Integer)get(color,"getId");
                    if(colorId!=0 && colorId!=7)
                        throw new UnsupportedOperationException("Unsupported color space id="+colorId+" (supported: sRGB/Display P3 SDR)");
                    Info after=capture.info();
                    if(!before.same(after)) {
                        if(!nativeError(fd,request[0],2,"Display changed during capture; frame discarded")) break;
                        continue;
                    }
                    if(!nativeFrame(fd,request[0],hardware,before.width,before.height,before.rotation,colorId)) break;
                } catch(Throwable error) {
                    String message=cause(error);
                    System.err.println("[YtblCapture] "+message);
                    if(!nativeError(fd,request[0],-1,message)) break;
                } finally {
                    closeBuffer(hardware);
                    // Gainmaps are not used by this SDR-only pipeline.
                    if(result!=null) try { closeBuffer(get(result,"getGainmap")); } catch(Exception ignored) {}
                }
            }
        } catch(Throwable error) {
            System.err.println("[YtblCapture] stopped: "+cause(error));
        }
    }
}
