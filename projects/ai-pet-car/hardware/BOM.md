# 元件清单（BOM）

价格为 **2026-11-26 在官网 / 授权店查到的单价（美元，不含税和运费）**，标「约」的是还没核实的估价，下单前以页面为准。选型原则：优先大牌、质量有保证，不为省钱买来路不明的模块。

**总预算**：必买约 **$300**（含税运费按 $330 准备），可选传感器约 **$33**。分两批买，第一批到货就能开始桌面阶段（L0–L3）。

## 第一批：桌面阶段（约 $145）

| # | 元件 | 型号 | 数量 | 单价 | 在哪买 | 用来干嘛 |
| :-: | --- | --- | :-: | --: | --- | --- |
| 1 | 主控板 | 乐鑫 ESP32-S3-DevKitC-1-N8R8（8 MB Flash + 8 MB PSRAM） | 1 | $19.95 | [Adafruit #5336](https://www.adafruit.com/product/5336)（目前缺货）/ DigiKey / Mouser | 小车的“大脑” |
| 2 | 麦克风 | Adafruit ICS-43434 I2S MEMS 麦克风 | 1 | $8.95 | [Adafruit #6049](https://www.adafruit.com/product/6049) | 听你说话 |
| 3 | 功放 | Adafruit MAX98357A I2S 3 W 功放 | 1 | $5.95 | [Adafruit #3006](https://www.adafruit.com/products/3006) | 推动喇叭 |
| 4 | 喇叭 | Adafruit 带腔体喇叭 3 W 4 Ω | 1 | $3.95 | [Adafruit #3351](https://www.adafruit.com/products/3351) | 说话 |
| 5 | 圆形屏幕 | Adafruit 1.28" 240×240 圆形 TFT（GC9A01A，EYESPI） | 1 | $17.50 | [Adafruit #6178](https://www.adafruit.com/product/6178) | 显示动漫表情 |
| 6 | 电机驱动 | Pololu TB6612FNG 双路电机驱动板 | 1 | $4.95 | [Pololu #713](https://www.pololu.com/product/713) | 控制两个电机 |
| 7 | 电机 | Pololu 50:1 Micro Metal Gearmotor HP 6V，带 12 CPR 编码器（后接口） | 2 | $29.95 | [Pololu #5160](https://www.pololu.com/product/5160) | 让轮子转，编码器测转速 |
| 8 | 编码器线 | Pololu 6 芯 JST SH 线（配 #5160） | 2 | 约 $3 | Pololu | 连接编码器 |
| 9 | 面包板 + 杜邦线 | 全尺寸面包板、公对公 / 公对母跳线 | 1 套 | 约 $15 | Adafruit / DigiKey | 先不焊接，插线测试 |

第一批小计：约 **$145**

## 第二批：装车阶段（约 $155）

| # | 元件 | 型号 | 数量 | 单价 | 在哪买 | 用来干嘛 |
| :-: | --- | --- | :-: | --: | --- | --- |
| 10 | 轮子 | Pololu Wheel 32×7 mm（一对） | 1 对 | $4.45 | [Pololu #1087](https://www.pololu.com/product/1087) | 驱动轮 |
| 11 | 万向球 | Pololu Ball Caster 3/8" 金属球 | 1 | $2.95 | [Pololu #951](https://www.pololu.com/product/951) | 第三个支点 |
| 12 | 电池 | Gens ace 2S 7.4 V 1000 mAh 45C 锂聚合物电池 | 1 | $13.19 | [GensTattu](https://genstattu.com/gens-ace-2s-1000mah-45c-lipo-battery-pack-with-deans-plug/) | 整车供电 |
| 13 | 充电器 | ISDT 608AC 平衡充电器 | 1 | $64.99 | [GetFPV](https://www.getfpv.com/isdt-608ac-smart-battery-charger-ac-50w-dc-200w-8a-w-detachable-power-supply.html) | 安全地给锂电池充电 |
| 14 | 防爆袋 | 锂电池防爆袋 | 1 | 约 $10 | GetFPV / 航模店 | 充电和存放电池 |
| 15 | 5 V 降压 | Pololu D24V50F5（5 V 5 A） | 1 | $32.95 | [Pololu #2851](https://www.pololu.com/product/2851) | 电池电压 → 5 V 给主控和功放 |
| 16 | 电容、开关、接头 | Panasonic / Nichicon 电解电容 470 µF、100 µF，船型开关，XT30 / Deans 接头 | 若干 | 约 $15 | DigiKey / Mouser | 稳压、总开关、接电池 |
| 17 | 底盘 | 亚克力板 / 3D 打印 + 铜柱螺丝 | 1 | 约 $10 | 学校 makerspace / 自己做 | 把所有东西固定在一起 |

第二批小计：约 **$155**

## 可选：让它更像宠物（约 $33）

| 元件 | 型号 | 单价 | 在哪买 | 用来干嘛 |
| --- | --- | --: | --- | --- |
| 陀螺仪 | Adafruit LSM6DSOX 6 轴 IMU | $11.95 | [Adafruit #4438](https://www.adafruit.com/products/4438) | 知道自己被拿起来、摔倒 |
| 测距 | Adafruit VL53L0X 激光测距 | 约 $15 | Adafruit | 前面有障碍就停 |
| 触摸 | Adafruit 电容触摸模块 | 约 $6 | Adafruit | 摸摸头有反应 |

## 下单前注意

> [!WARNING]
> - **麦克风 ICS-43434 已被 Adafruit 标为停产**，目前还有库存，建议第一批尽早买；买不到就换 Adafruit SPH0645（#3421，接线和用法基本一样）。
> - **主控板 Adafruit 缺货**时去 DigiKey 或 Mouser 买乐鑫官方的同型号，认准 `ESP32-S3-DevKitC-1-N8R8`，别买成 N16R8V（1.8 V 版本）。
> - **电池接头**：Gens ace 这款默认是 Deans（T 型）接头，买对应的公头，或者换成 XT30 版本，和第 16 项保持一致。
> - **锂电池安全**：只用平衡充电器充电，充电时放防爆袋里、有人看着，鼓包的电池不要再用。

## 建议的下单方式

把同一家店的东西凑一单，省运费：

1. **Adafruit**：麦克风、功放、喇叭、屏幕、面包板跳线（+ 可选传感器）
2. **Pololu**：电机驱动、电机 ×2、编码器线、轮子、万向球、降压模块
3. **DigiKey / Mouser**：主控板（Adafruit 缺货时）、电容、开关、接头
4. **航模店（GetFPV / GensTattu）**：电池、充电器、防爆袋
