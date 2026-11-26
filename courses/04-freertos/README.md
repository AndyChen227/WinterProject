<img src="../../projects/ai-pet-car/media/art/mascot-wink.svg" width="90" align="right">

# ⚙️ 04 · FreeRTOS

| 📌 | 说明 |
| --- | --- |
| **🗓️ 时间** | 2027.01 |
| **🎯 完成标准** | 宠物小车代码拆成音频、网络、显示、电机几个任务，用队列传指令 |

> [!NOTE]
> ESP-IDF 底层就是 FreeRTOS，所以在 ESP32 上直接学。

## 🧠 知识点

- [ ] 为什么需要 RTOS：裸机大循环的局限
- [ ] ESP-IDF 里的 FreeRTOS：`xTaskCreatePinnedToCore`，双核怎么分任务
- [ ] 任务：创建、优先级、栈大小、任务状态
- [ ] 调度：抢占式、时间片、`vTaskDelay` vs `vTaskDelayUntil`
- [ ] 队列：任务间传数据
- [ ] 信号量：二值信号量、计数信号量，中断里怎么通知任务
- [ ] 互斥量与优先级反转
- [ ] 软件定时器
- [ ] 中断里能调用哪些 API（`FromISR` 版本）
- [ ] 栈溢出检测、看任务占用

## 💪 练习建议

先做三个任务：LED 闪烁、串口打印、按键检测，用队列把按键事件传给打印任务。跑通后再把宠物小车的代码拆成任务。
