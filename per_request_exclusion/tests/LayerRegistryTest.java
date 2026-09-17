package com.ytbl.capture;
import java.lang.reflect.Array;
import java.util.HashMap;
import java.util.Map;

public final class LayerRegistryTest {
    public static final class FakeSurface {
        static long next=1000;
        static final Map<Long,Integer> handles=new HashMap<>();
        static int allocated,released;
        long object;
        public FakeSurface(){}
        public FakeSurface(FakeSurface source,String site){
            if(!source.isValid())throw new IllegalStateException("invalid source");
            object=++next;handles.put(object,handles.get(source.object));++allocated;
        }
        private static long nativeCopyFromSurfaceControl(long pointer){
            if(pointer<=0)return 0;
            long p=++next;handles.put(p,(int)pointer);++allocated;return p;
        }
        private void assignNativeObject(long pointer,String site){object=pointer;}
        public void release(){if(object!=0){handles.remove(object);object=0;++released;}}
        public boolean isValid(){return object!=0 && handles.containsKey(object);}
    }
    static int tests=0;
    static void check(boolean condition,String label){if(!condition)throw new AssertionError(label);++tests;}
    public static void main(String[] args)throws Exception{
        LayerRegistry r=new LayerRegistry(FakeSurface.class);
        try{r.snapshot();throw new AssertionError("empty exclusion accepted");}catch(IllegalStateException ok){++tests;}
        long g1=r.register(1,101,800,600);check(r.count()==1,"first registration");
        LayerRegistry.Snapshot first=r.snapshot();check(first.count==1 && first.current(),"snapshot");
        Object item=Array.get(first.array,0);check(((FakeSurface)item).isValid(),"snapshot owns live copy");
        long g2=r.register(2,202,800,600);check(g2>g1 && !first.current(),"new layer invalidates old capture");
        LayerRegistry.Snapshot second=r.snapshot();check(second.count==2,"all owned windows excluded");
        r.unregister(1);check(!second.current() && r.count()==1,"destroy invalidates generation");
        check(((FakeSurface)item).isValid(),"destroying original does not invalidate in-flight copy");
        first.close();first.close();check(!((FakeSurface)item).isValid(),"request releases exactly once");
        second.close();
        r.register(2,303,800,600);check(r.count()==1,"rebind replaces registry copy");
        LayerRegistry.Snapshot third=r.snapshot();check(third.current(),"replacement snapshot current");
        r.clear();check(!third.current() && r.count()==0,"clear invalidates request");
        check(((FakeSurface)Array.get(third.array,0)).isValid(),"clear retains in-flight ownership");
        third.close();check(FakeSurface.allocated==FakeSurface.released,"no fixture reference leak");
        System.out.println("PASS "+tests+" exclusion registry assertions (JVM fixtures, not Android runtime)");
    }
}
