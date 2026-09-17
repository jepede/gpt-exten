package com.ytbl.capture;

import java.lang.reflect.Array;
import java.lang.reflect.Constructor;
import java.lang.reflect.Method;
import java.util.LinkedHashMap;
import java.util.Map;

/** Only accepts pointers registered synchronously by this process's own creator.
 * A native SurfaceControl pointer is NEVER serialized to another process.
 * The platform copy operation takes its own native reference; per-request copies
 * remain valid while the original window is being destroyed or rebound.
 */
final class LayerRegistry {
    private final Class<?> type;
    private final Constructor<?> empty, copy;
    private final Method nativeCopy, assign, release, valid;
    private final Map<Long,Object> layers=new LinkedHashMap<>();
    private long generation=0;
    private boolean healthy=true;

    LayerRegistry(Class<?> surfaceType) throws Exception {
        type=surfaceType;
        empty=type.getDeclaredConstructor(); empty.setAccessible(true);
        copy=type.getDeclaredConstructor(type,String.class); copy.setAccessible(true);
        nativeCopy=type.getDeclaredMethod("nativeCopyFromSurfaceControl",long.class); nativeCopy.setAccessible(true);
        assign=type.getDeclaredMethod("assignNativeObject",long.class,String.class); assign.setAccessible(true);
        release=type.getMethod("release"); valid=type.getMethod("isValid");
    }
    synchronized long register(long key,long pointer,int width,int height) throws Exception {
        ++generation;
        if(key==0 || pointer==0 || width<1 || height<1) {
            healthy=false;throw new IllegalArgumentException("Invalid owned surface registration");
        }
        Object surface=empty.newInstance();
        long clone=(Long)nativeCopy.invoke(null,pointer);
        if(clone==0){healthy=false;throw new IllegalStateException("Cannot copy the owned native SurfaceControl");}
        try {
            assign.invoke(surface,clone,"Ytbl owned surface exclusion");
            if(!Boolean.TRUE.equals(valid.invoke(surface))) throw new IllegalStateException("Invalid exclusion SurfaceControl");
            Object previous=layers.put(key,surface);
            if(previous!=null)release.invoke(previous);
            return generation;
        } catch(Exception error) {
            healthy=false;
            // Successful assign registers the platform finalizer. Never manually
            // decStrong an unverified JNI reference or guess RefBase offsets.
            try { if(Boolean.TRUE.equals(valid.invoke(surface)))release.invoke(surface); } catch(Exception ignored) {}
            throw error;
        }
    }
    synchronized long unregister(long key) throws Exception {
        ++generation;
        Object surface=layers.remove(key);
        if(surface!=null)release.invoke(surface);
        return generation;
    }
    synchronized int count(){return healthy ? layers.size() : -1;}
    synchronized long generation(){return generation;}
    synchronized void clear() {
        ++generation;
        for(Object surface:layers.values())try {release.invoke(surface);}catch(Exception ignored){}
        layers.clear();
    }
    synchronized Snapshot snapshot() throws Exception {
        if(!healthy || layers.isEmpty()) throw new IllegalStateException("No valid owned surfaces to exclude; unfiltered capture refused");
        Object result=Array.newInstance(type,layers.size());int at=0;
        try {
            for(Object surface:layers.values()) {
                if(!Boolean.TRUE.equals(valid.invoke(surface)))throw new IllegalStateException("An exclusion surface was released");
                Object own=copy.newInstance(surface,"Ytbl per-request exclusion");
                Array.set(result,at++,own);
                if(!Boolean.TRUE.equals(valid.invoke(own)))throw new IllegalStateException("Invalid per-request exclusion copy");
            }
            return new Snapshot(this,result,generation,layers.size());
        } catch(Exception error) {
            for(int i=0;i<at;++i)try {release.invoke(Array.get(result,i));}catch(Exception ignored){}
            throw error;
        }
    }
    static final class Snapshot implements AutoCloseable {
        final LayerRegistry owner;
        final Object array;
        final long generation;
        final int count;
        private boolean closed;
        Snapshot(LayerRegistry r,Object a,long g,int n){owner=r;array=a;generation=g;count=n;}
        boolean current(){return owner.generation()==generation && owner.count()==count;}
        @Override public void close() {
            if(closed)return;closed=true;
            for(int i=0;i<count;++i)try {owner.release.invoke(Array.get(array,i));}catch(Exception ignored){}
        }
    }
}
