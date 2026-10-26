# 王者荣耀 12.1.1.1：核心坐标模块静态逆向

源 APK 按 HTTP Range 读取；只提取必要成员，逐一验证 ZIP CRC32 和 SHA256。未验证整个 APK 的 MD5/SHA256。

## 实际导出文件

| 文件 | 字节数 | SHA256 | ZIP 大小 |
|---|---:|---|---:|
| lib/arm64-v8a/libil2cpp.so | 227661664 | 6e00c3ac8ac129d7b6dd5bdd5c8c72777d70a91a317d193bf5f422505d9bafd5 | 77648131 |
| lib/arm64-v8a/libGameCore.so | 86426392 | dc034883ea2fc5c6be42d2e3b068652a7e1829f73450bb732fceebbd8f75d4c8 | 21200454 |
| lib/arm64-v8a/libunity.so | 30220440 | 6f862b245e048e8062b71c747d817bbb942276039bf6991adea60046b19b68a8 | 13956734 |
| assets/bin/Data/Managed/Metadata/global-metadata.dat | 60322264 | 5e66b7a0597679b6ef0383755eee4adb60a71f15a87a6fab91582eaa7f85a3a7 | 17342950 |

## IL2CPP 元数据

Magic: af1bb1fa
Version: 29
Standard metadata: True

## 字符串证据（仅做定位，不等于确认加密）

### il2cpp
- Vector3: 180+
- Vector2: 180+
- Transform: 180+
- GetPosition: 11
- SetPosition: 15
- LocalPosition: 3
- m_Position: 1
- Position: 127
- Coord: 4
- Coordinate: 1
- Location: 16
### gamecore
- Vector3: 11
- Vector2: 2
- Transform: 57
- GetPosition: 2
- SetPosition: 5
- LocalPosition: 1
- ActorPosition: 15
- ActorPos: 17
- HeroPos: 9
- HeroPosition: 6
- Position: 180+
- Coord: 16
- Coordinate: 5
- Location: 61
- ActorRoot: 98
- HeroActor: 3
- BattleActor: 2
- ActorManager: 8
- ActorComponent: 6
- MoveDir: 34
- MoveSpeed: 51
- FrameSync: 10
- SyncPosition: 1
### unity
- Vector3: 24
- Vector2: 15
- Transform: 180+
- GetPosition: 18
- SetPosition: 24
- LocalPosition: 15
- m_Position: 5
- Position: 180+
- Coord: 37
- Coordinate: 7
- Location: 35
### metadata
- Vector3: 180+
- Vector2: 110
- Transform: 180+
- GetPosition: 43
- SetPosition: 56
- WorldPosition: 34
- LocalPosition: 57
- m_Position: 21
- ActorPosition: 8
- ActorPos: 22
- HeroPos: 68
- HeroPosition: 31
- Position: 180+
- Coord: 180+
- Coordinate: 106
- Location: 180+
- ActorRoot: 4
- HeroActor: 15
- GameActor: 5
- BattleActor: 4
- ActorManager: 8
- ActorComponent: 14
- MoveController: 1
- MoveDir: 51
- MoveSpeed: 48
- PlayerPosition: 6
- GetActorPos: 2
- FrameSync: 15
- SyncPosition: 3
- GameBattle: 14

## 分析限制
查到 Vector3、Position 或 Encrypt 字符串，不代表它们之间存在真实调用或坐标加密。需要继续做 IL2CPP 类型/方法解析、ARM64 控制流和真实样本回归。
