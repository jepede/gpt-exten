#pragma once
#include <cstdint>
#include <memory>
#include <string>

namespace livebg {
struct Config {
    int width=0,height=0,rotation=0;
    float scale=0.5f;
    int maxFps=15;
};
struct TextureFrame {
    unsigned texture=0;
    int textureWidth=0,textureHeight=0,displayWidth=0,displayHeight=0,rotation=0;
    uint64_t readyNs=0;
    bool hdr=false;
};
struct Status {
    bool workerRunning=false;
    unsigned received=0;
    double captureFps=0;
    std::string error;
};
// Methods except internal worker code run on the existing EGL/ImGui render thread.
// Stop BEFORE EGL teardown. No permission changes are performed by this class.
class Session {
public:
    Session();
    ~Session();
    Session(const Session&)=delete;
    Session& operator=(const Session&)=delete;
    bool Start(const std::string& runtimeDirectory,const Config& config,bool ownLayersExcluded);
    void Configure(const Config& config);
    bool Poll(TextureFrame& result); // Nonblocking; false for errors/stale/rotating frames.
    Status GetStatus() const;
    void Stop();
private:
    struct Impl;
    std::unique_ptr<Impl> impl_;
};
}
