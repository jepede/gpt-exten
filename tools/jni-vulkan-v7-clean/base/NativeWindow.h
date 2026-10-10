#pragma once
#include "VulkanOverlay.h"
#include <atomic>
#include <cmath>
#include <unistd.h>
#include <new>
#include <condition_variable>
#include <mutex>
#include <cstdint>
#include <algorithm>
#include <chrono>
#include <exception>
#include <functional>
#include <memory>
#include <thread>
#include <android/native_window.h>
#include <android/native_window_jni.h>
#include <android/surface_control.h>

struct sConfig {
    struct sMenu {
        bool Bones;
        bool Line;
        bool Box;
        bool Health;
        bool Name;
        bool Distance;
        bool TeamID;
        bool Vehicle;
		bool Radar;
    };
    sMenu Menu{0};
	
	struct sRadar {
        float x;
		float y;
    };
    sRadar Radar{0};
};
sConfig Config{0};

void BeginDraw() {

    ImGui::Begin("Mind Mod");
    
    ImGui::Checkbox("方框", &Config.Menu.Box);
    ImGui::SameLine();
    ImGui::Checkbox("射线", &Config.Menu.Line);
    ImGui::SameLine();
    ImGui::Checkbox("骨骼", &Config.Menu.Bones);
    ImGui::SameLine();
    ImGui::Checkbox("距离", &Config.Menu.Distance);

    ImGui::Checkbox("名称", &Config.Menu.Name);
    ImGui::SameLine();
    ImGui::Checkbox("血量", &Config.Menu.Health);
    ImGui::SameLine();
    ImGui::Checkbox("阵营", &Config.Menu.TeamID);
    ImGui::SameLine();
    ImGui::Checkbox("雷达", &Config.Menu.Radar);

    ImGui::Spacing(); // 间距

    ImGui::SliderFloat("雷达 X", &Config.Radar.x, 0.0f, VulkanState.ScreenWidth, "%.2f", 1.0f);
    ImGui::SliderFloat("雷达 Y", &Config.Radar.y, 0.0f, VulkanState.ScreenHeight, "%.2f", 1.0f);

    ImGui::Separator();
    ImGui::Text("绘制耗时 %.3f ms (%.1f FPS)", 1000.0f / ImGui::GetIO().Framerate, ImGui::GetIO().Framerate);
                    
    ImGui::End();
}



// Durable multi-parent Vulkan presentation and window lifetime management.
#include "OverlaySupervisor.h"
