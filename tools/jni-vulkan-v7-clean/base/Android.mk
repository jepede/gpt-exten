LOCAL_PATH := $(call my-dir)
BUILD_MODE ?= debug

include $(CLEAR_VARS)
LOCAL_MODULE := dobby
LOCAL_SRC_FILES := Library/dobby/$(TARGET_ARCH_ABI)/libdobby.a
LOCAL_EXPORT_C_INCLUDES := $(LOCAL_PATH)/Library/dobby/include
include $(PREBUILT_STATIC_LIBRARY)

include $(CLEAR_VARS)
LOCAL_MODULE := Android
LOCAL_CPPFLAGS := -std=c++20 -fexceptions -Werror=format-security -Werror=return-type -Wno-error=c++11-narrowing
LOCAL_C_INCLUDES += $(LOCAL_PATH)
LOCAL_C_INCLUDES += $(LOCAL_PATH)/third_party/imgui
LOCAL_C_INCLUDES += $(LOCAL_PATH)/third_party/imgui/backends
LOCAL_C_INCLUDES += $(LOCAL_PATH)/Library/Imgui/include
LOCAL_C_INCLUDES += $(LOCAL_PATH)/Library/dobby/include
LOCAL_SRC_FILES := Injector.cpp \
    third_party/imgui/imgui.cpp \
    third_party/imgui/imgui_draw.cpp \
    third_party/imgui/imgui_tables.cpp \
    third_party/imgui/imgui_widgets.cpp \
    third_party/imgui/backends/imgui_impl_vulkan.cpp
LOCAL_LDLIBS := -llog -landroid -lvulkan -ldl -lm
LOCAL_LDFLAGS += -Wl,--exclude-libs,ALL -Wl,--build-id
LOCAL_STATIC_LIBRARIES := dobby

ifeq ($(BUILD_MODE),debug)
    LOCAL_CPPFLAGS += -g -O0 -frtti -fvisibility=default -fno-omit-frame-pointer
    # Stable default: parent auto-switching must be explicitly enabled via setprop.
    LOCAL_CPPFLAGS += -DYS_DEFAULT_AUTO_PROBE=0
    LOCAL_LDFLAGS += -Wl,--export-dynamic
else ifeq ($(BUILD_MODE),release)
    LOCAL_CPPFLAGS += -O2 -fno-rtti -fvisibility=hidden -fomit-frame-pointer
    LOCAL_CPPFLAGS += -DYS_DEFAULT_AUTO_PROBE=0
    LOCAL_LDFLAGS += -Wl,-s
else
    $(error BUILD_MODE must be debug or release)
endif
include $(BUILD_SHARED_LIBRARY)
