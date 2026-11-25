# AI Pet Car

一台能对话的 AI 电子宠物小车：对它说话，它用声音回应，圆形屏幕上的动漫小人跟着变表情；让它“转圈”“往前跑”，它就会动。

基于 ESP32-S3 + FreeRTOS（ESP-IDF），语音经云端大模型（DeepSeek / Claude）处理。参考开源项目“小智 AI”（xiaozhi-esp32）。项目尚未开始，下面是计划。

## 工作原理

```
你说话 → 麦克风(I2S) → ESP32-S3 → Wi-Fi → 云端：语音识别 → 大模型 → 语音合成
                                                          │
屏幕表情(SPI) ← 电机动作(PWM) ← 喇叭播放(I2S) ← ESP32-S3 ←─┘  回复语音 + 动作指令
```

## 目标功能

阶段划分参考了已经做成的开源项目（小智 xiaozhi-esp32、ESP-SparkBot、aibot、esp32-s3-ai-robot 等），调研见[这份文档](https://claude.ai/artifact/2MzYh5NDjD8tnHYwonAe8V)。共同规律是先在面包板上把所有模块跑通，软件全部能用了再装上车身。

- [ ] L0 硬件验收：面包板接好主控、麦克风、功放、圆屏，用 8 MB 分区编译小智的 `bread-compact-wifi-lcd`（屏幕选 GC9A01）烧进去，能和 xiaozhi.me 对话、屏上有表情
- [ ] L1 上手：ESP-IDF v6.x 环境、点灯、串口、按键中断，加一个串口命令行用来手动测每个模块
- [ ] L2 表情 + 电机：LVGL 在圆屏上播 3–4 个表情；TB6612 PWM 控制前进、后退、原地转圈（车轮架空调）；用万用表量一次电机启动电流
- [ ] L3 听和说 + 最小服务端：先做音频回环（录音传到电脑存 WAV、电脑的 WAV 传回来播放）；再写一个最小 Python 服务（语音识别 → DeepSeek / Claude → edge-tts），ESP32 通过 WebSocket 收发音频，先用按键说话；测一次延迟
- [ ] L4 语音控制 + 上车：服务端用 function calling 定义 `move(direction, duration_ms)`、`spin(turns)`、`set_emotion(name)` 等工具，下发 JSON；ESP32 端用动作队列，每个动作限时，收不到心跳就停车；FreeRTOS 拆成音频、网络、显示、电机任务；装上底盘和 2S 电池
- [ ] L5 完善（挑着做）：离线唤醒词（ESP-SR WakeNet）、本地宠物状态机（断网也会眨眼）、IMU 检测被拿起、测距避障、编码器 + PID 精准转圈、Opus 流式传输降延迟、电源做成自己的 PCB

## 硬件

优先大牌、质量有保证的型号。必买件约 $275（含税运费按 $300 准备），可选传感器约 $35；桌面阶段（L0–L3）先买前 6 项，约 $130。

| 部件 | 型号 | 用途 |
| --- | --- | --- |
| 主控 | 乐鑫官方 ESP32-S3-DevKitC-1-N8R8（8 MB Flash + 8 MB Octal PSRAM；GPIO35–37 不可用） | 主控 |
| 麦克风 | Adafruit I2S MEMS Microphone ICS-43434 | 听 |
| 功放 + 喇叭 | Adafruit MAX98357A + 4 Ω 3 W 喇叭 | 说 |
| 表情屏 | Adafruit 1.28" 240×240 圆形 TFT（GC9A01A，EYESPI） | 表情 |
| 电机驱动 | Pololu TB6612FNG 驱动板 | 驱动电机 |
| 电机 | Pololu 50:1 Micro Metal Gearmotor HP 6V（带 12 CPR 编码器）×2 + Pololu 轮子、万向球 | 车身 |
| 电池 + 充电 | 2S 7.4 V 锂聚合物电池（Gens ace / Ovonic）+ ISDT 608AC 平衡充电器 + 防爆袋 | 供电 |
| 5 V 电源 | Pololu D24V50F5（5 V 5 A 降压） | 给 ESP32 和功放 |
| 其他 | Panasonic / Nichicon 电解电容（TB6612 VM 旁 470 µF，ESP32 5 V 旁 100 µF）、总开关、XT30 接头 | 去耦、开关 |
| 可选 | Adafruit LSM6DSOX IMU、Adafruit VL53L0X 测距、Adafruit 电容触摸模块 | 让它更像宠物 |

供电方式：电池直接给 TB6612 的 VM（软件限制 PWM 占空比保护 6 V 电机），再经降压给 ESP32 和功放，两边分开，避免电机启动拉低电压导致重启。桌面阶段用 USB 供电，电机单独接电池。

## 计划目录

```
ai-pet-car/
├── firmware/    # ESP-IDF 工程
├── server/      # 服务端（L5 再做）
├── hardware/    # 接线图、引脚分配、电源设计
├── docs/        # 设计说明、调试记录、测试数据
└── media/       # 照片、演示视频
```

## 结果（完成后填写）

- 说话到开始回复的延迟：
- 支持的动作指令：
- 续航：
- 演示视频：
