# 03 · ESP32 入门

时间：寒假第 1–3 周
硬件：ESP32-S3 开发板（N16R8）
工具：ESP-IDF（官方框架，C 语言，VS Code 插件安装最方便）
完成标准：宠物小车的屏幕能显示表情、电机能前进后退转圈，按键可以切换

> 为什么不是 STM32：宠物小车要连 Wi-Fi 跑大模型对话，ESP32-S3 自带 Wi-Fi，内存也够跑音频和屏幕。中断、定时器、I2C/SPI 这些概念在两种芯片上是通用的，面试问 STM32 时你也能讲。

## 知识点

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
- [ ] SPI：驱动 GC9A01 圆形屏
- [ ] LVGL（或直接画图）：在屏幕上显示表情图片和简单动画
- [ ] I2S：INMP441 麦克风录音、MAX98357A 喇叭播放
- [ ] I2C：读一个传感器（可选）
- [ ] Wi-Fi：连上路由器，发 HTTP 请求
- [ ] NVS：掉电保存配置（比如 Wi-Fi 密码）

### 概念
- [ ] 中断与回调，中断里不能做耗时操作
- [ ] 轮询、中断、DMA 三种方式的区别
- [ ] Flash 和 PSRAM 的区别，大块数据为什么放 PSRAM

## 练习建议

每个外设在 `code/` 下放一个最小可运行示例，笔记里记录接线（哪个引脚接哪里）和关键配置。
