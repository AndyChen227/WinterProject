<sub>[📚 课程](../README.md) › 03 · ESP32 入门</sub>

<img src="../../projects/ai-pet-car/media/art/mascot-star.svg" width="90" align="right">

# 🔌 03 · ESP32 入门

> 在真正的芯片上写 C：点灯、读按键、驱动屏幕和电机、连 Wi-Fi。

| 🗓️ 时间 | 🔧 硬件 | 🧰 工具 | 🎯 完成标准 |
| --- | --- | --- | --- |
| 寒假第 1–3 周 | ESP32-S3-DevKitC-1-N8R8<br><sub>购买见 [元件清单](../../projects/ai-pet-car/hardware/BOM.md)</sub> | ESP-IDF<br><sub>官方框架，VS Code 插件安装</sub> | 屏幕能显示表情<br>电机能前进后退转圈<br>按键可以切换 |

> [!TIP]
> **为什么不是 STM32**：宠物小车要连 Wi-Fi 跑大模型对话，ESP32-S3 自带 Wi-Fi，内存也够跑音频和屏幕。中断、定时器、I2C/SPI 这些概念在两种芯片上是通用的，面试问 STM32 时你也能讲。

## 📒 笔记

| # | 知识点 | 笔记 | 代码 | 日期 | 掌握 |
| :-: | --- | :-: | :-: | :-: | :-: |
| | <sub>还没有笔记，学完第一个知识点后在这里加一行</sub> | | | | |

## 🧠 知识点

### 开发环境
- [ ] 安装 ESP-IDF（VS Code 插件），编译烧录 `hello_world` 示例
- [ ] `idf.py build / flash / monitor`，看串口日志
- [ ] `menuconfig` 配置项目，开启 PSRAM
- [ ] 读懂一个 ESP-IDF 工程的结构：`main/`、`components/`、`CMakeLists.txt`

### 外设
- [ ] GPIO：点亮 LED、读按键
- [ ] GPIO 中断：按键中断
- [ ] UART：串口收发
- [ ] LEDC / MCPWM：PWM 控制电机转速和方向
- [ ] SPI：驱动 ST7796S 3.5 寸屏（320×480）
- [ ] LVGL（或直接画图）：在屏幕上显示表情图片和简单动画
- [ ] I2S：ICS-43434 麦克风录音、MAX98357A 喇叭播放
- [ ] I2C：读一个传感器（可选）
- [ ] Wi-Fi：连上路由器，发 HTTP 请求
- [ ] NVS：掉电保存配置（比如 Wi-Fi 密码）

### 概念
- [ ] 中断与回调，中断里不能做耗时操作
- [ ] 轮询、中断、DMA 三种方式的区别
- [ ] Flash 和 PSRAM 的区别，大块数据为什么放 PSRAM

## 💪 练习建议

每个外设在 `code/` 下放一个最小可运行示例，笔记里记录接线（哪个引脚接哪里）和关键配置。

---

<p align="center"><sub><a href="../02-c-advanced">← 📗 02 · C 进阶</a> &nbsp;·&nbsp; <a href="../README.md">📚 课程总览</a> &nbsp;·&nbsp; <a href="../04-freertos">⚙️ 04 · FreeRTOS →</a></sub></p>
