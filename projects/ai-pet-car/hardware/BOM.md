<sub>[🏠 首页](../../../README.md) › [🛠️ 项目](../../README.md) › [🐱 AI 电子宠物小车](../README.md) › [🔌 硬件](README.md) › 🛒 元件清单</sub>

<img src="../media/art/mascot-love.svg" width="90" align="right">

# 🛒 元件清单（BOM）

> 做小车要买什么、在哪买、花多少钱，到货后哪些要自己焊。

价格为 **2026-11-26 在官网 / 授权店查到的单价（美元，不含税和运费）**，标「约」的是还没核实的估价，下单前以页面为准。选型原则：优先大牌、质量有保证，不为省钱买来路不明的模块。

| 💰 花多少 | 🛒 买什么 | 🧾 怎么买 | 🪛 到货后 |
| --- | --- | --- | --- |
| [预算](#budget) | [第一批：桌面阶段](#batch1)<br>[第二批：装车阶段](#batch2)<br>[可选：让它更像宠物](#optional)<br>[工具与耗材](#tools) | [下单前注意](#notice)<br>[建议的下单方式](#order) | [哪些要自己焊](#solder) |

<a id="budget"></a>

## 💰 预算

| 方案 | 合计 | 含税运费按此准备 |
| --- | --: | --: |
| 🏫 元件 + 基础工具，焊接去学校 MILL 免费做 | 约 $407 | $460 |
| 🏠 元件 + 基础工具 + 自己买一套焊接工具 | 约 $622 | $695 |

可选传感器另加约 $33。元件分两批买，第一批到货就能开始桌面阶段（L0–L3）。

**钱花在哪**

| 项目 | 金额 |
| --- | --: |
| 第一批元件 | 约 $129 |
| 第二批元件 | 约 $155 |
| 基础工具 | 约 $121 |
| 🏫 **小计（焊接去 MILL）** | **约 $407** |
| 焊接工具（自己买） | 约 $215 |
| 🏠 **小计（自己买焊接工具）** | **约 $622** |
| 可选传感器 | 约 $33 |

工具是一次性投入，以后做别的硬件项目还能接着用。

<a id="batch1"></a>

## 📦 第一批：桌面阶段（约 $129）

| # | 元件 | 型号 | 数量 | 单价 | 在哪买 | 用来干嘛 |
| :-: | --- | --- | :-: | --: | --- | --- |
| 1 | 主控板 | 乐鑫 ESP32-S3-DevKitC-1-N8R8（8 MB Flash + 8 MB PSRAM） | 1 | $19.95 | [Adafruit #5336](https://www.adafruit.com/product/5336)（目前缺货）/ DigiKey / Mouser | 小车的“大脑” |
| 2 | 麦克风 | Adafruit ICS-43434 I2S MEMS 麦克风 | 1 | $8.95 | [Adafruit #6049](https://www.adafruit.com/product/6049) | 听你说话 |
| 3 | 功放 | Adafruit MAX98357A I2S 3 W 功放 | 1 | $5.95 | [Adafruit #3006](https://www.adafruit.com/products/3006) | 推动喇叭 |
| 4 | 喇叭 | Adafruit 带腔体喇叭 3 W 4 Ω | 1 | $3.95 | [Adafruit #3351](https://www.adafruit.com/products/3351) | 说话 |
| 5 | 屏幕 | Waveshare 3.5" IPS 电容触摸屏，320×480（驱动 ST7796S，触摸 FT6336U，SPI + I2C），SKU 29318 | 1 | $18.99 | [Waveshare 官网](https://www.waveshare.com/3.5inch-Capacitive-Touch-LCD.htm) | 竖着装，显示动漫少女半身形象；能感应摸摸 |
| 6 | 电机驱动 | Pololu TB6612FNG 双路电机驱动板 | 1 | $4.95 | [Pololu #713](https://www.pololu.com/product/713) | 控制两个电机 |
| 7 | 电机 | Pololu 50:1 Micro Metal Gearmotor HP 6V，带 12 CPR 编码器（后接口） | 2 | $29.95 | [Pololu #5160](https://www.pololu.com/product/5160) | 让轮子转，编码器测转速 |
| 8 | 编码器线 | Pololu 6 芯 JST SH 单头线 30 cm（#4763，另一头是散线，目前缺货） | 2 | $3.00 | [Pololu 编码器线](https://www.pololu.com/category/277/6-pin-jst-sh-style-cables-for-micro-metal-gearmotor-encoders) | 连接电机和编码器 |

第一批小计：约 **$129**

> [!NOTE]
> **为什么屏幕选 Waveshare 3.5 寸**（2026-11-26 对比过）
> - 同类开源项目大多用 1.3–2.4 寸（SparkBot、Otto 是 240×240，Stack-chan、ESP-BOX-3 是 320×240），3.5 寸竖屏才放得下一个半身角色。
> - 它是 **IPS** 屏，从侧面看颜色不发白；带**电容触摸**，以后可以做“摸摸头”。
> - 驱动芯片 **ST7796S** 很主流：小智固件直接支持（`ST7796 320*480 IPS`），乐鑫 ESP-IDF 和 LVGL 都有现成驱动，资料多，新手最好上手。
> - 对比过的其他牌子：Adafruit #5846（3.5" 电容触摸，$39.95）缺货，页面也没写是 IPS；DFRobot DFR1092（3.5" IPS 全贴合，$29.90）屏幕本身做工更好，但官方没写驱动芯片，库里对应的是 ST7365P / ILI9488，小智不支持，对新手不友好。
> - Waveshare 是做了十几年开发板和屏幕的老牌子，每个模块都有官方 wiki 和 ESP32 示例。

<a id="batch2"></a>

## 🚗 第二批：装车阶段（约 $155）

| # | 元件 | 型号 | 数量 | 单价 | 在哪买 | 用来干嘛 |
| :-: | --- | --- | :-: | --: | --- | --- |
| 9 | 轮子 | Pololu Wheel 32×7 mm（一对） | 1 对 | $4.45 | [Pololu #1087](https://www.pololu.com/product/1087) | 驱动轮 |
| 10 | 万向球 | Pololu Ball Caster 3/8" 金属球 | 1 | $2.95 | [Pololu #951](https://www.pololu.com/product/951) | 第三个支点 |
| 11 | 电池 | Gens ace 2S 7.4 V 1000 mAh 45C 锂聚合物电池 | 1 | $13.19 | [GensTattu](https://genstattu.com/gens-ace-2s-1000mah-45c-lipo-battery-pack-with-deans-plug/) | 整车供电 |
| 12 | 充电器 | ISDT 608AC 平衡充电器 | 1 | $64.99 | [GetFPV](https://www.getfpv.com/isdt-608ac-smart-battery-charger-ac-50w-dc-200w-8a-w-detachable-power-supply.html) | 安全地给锂电池充电 |
| 13 | 防爆袋 | 锂电池防爆袋 | 1 | 约 $10 | GetFPV / 航模店 | 充电和存放电池 |
| 14 | 5 V 降压 | Pololu D24V50F5（5 V 5 A） | 1 | $32.95 | [Pololu #2851](https://www.pololu.com/product/2851) | 电池电压 → 5 V 给主控和功放 |
| 15 | 电容、开关、接头 | Panasonic / Nichicon 电解电容 470 µF、100 µF，船型开关，XT30 / Deans 接头 | 若干 | 约 $15 | DigiKey / Mouser | 稳压、总开关、接电池 |
| 16 | 底盘 | 亚克力板 / 3D 打印 + 铜柱螺丝 | 1 | 约 $10 | 学校 makerspace / 自己做 | 把所有东西固定在一起 |

第二批小计：约 **$155**

<a id="optional"></a>

## ✨ 可选：让它更像宠物（约 $33）

| 元件 | 型号 | 单价 | 在哪买 | 用来干嘛 |
| --- | --- | --: | --- | --- |
| 陀螺仪 | Adafruit LSM6DSOX 6 轴 IMU | $11.95 | [Adafruit #4438](https://www.adafruit.com/products/4438) | 知道自己被拿起来、摔倒 |
| 测距 | Adafruit VL53L0X 激光测距 | 约 $15 | Adafruit | 前面有障碍就停 |
| 触摸 | Adafruit 电容触摸模块 | 约 $6 | Adafruit | 摸摸头有反应 |

<a id="tools"></a>

## 🧰 工具与耗材

做这个项目之前手边什么工具都没有也没关系，下面分成两组。

### 🔧 基础工具（必买，约 $121）

不管焊不焊，这些都会天天用到。

| 工具 | 型号 | 数量 | 单价 | 在哪买 | 用来干嘛 |
| --- | --- | :-: | --: | --- | --- |
| 面包板 | Adafruit 全尺寸 830 孔 | 1 | $5.95 | [Adafruit #239](https://www.adafruit.com/product/239) | 不焊接就能把模块插在一起测试 |
| 跳线 | Adafruit 公对公跳线 | 2 包 | $3.95 | [Adafruit #758](https://www.adafruit.com/category/471) | 面包板上连线 |
| USB 数据线 | USB-A 转 Micro-B（开发板是 Micro-USB 口） | 1 | $2.95 | [Adafruit #592](https://www.adafruit.com/product/592)（目前缺货） | 烧录程序、看串口日志 |
| 万用表 | Fluke 106 | 1 | $78.47 | [Home Depot](https://www.homedepot.com/p/341461783) | 量电压、通断、电机电流，排查硬件问题全靠它 |
| 斜口钳 | Hakko CHP-170 | 1 | 约 $6 | DigiKey / Amazon | 剪线、剪掉多余的引脚 |
| 剥线钳 | Klein 11057（20–30 AWG 细线） | 1 | 约 $20 | [DigiKey](https://www.digikey.com/en/products/detail/klein-tools-inc/11057/6804879) | 剥细导线的皮 |

> [!TIP]
> USB 线一定要能传数据。有些线只能充电，插上电脑认不出开发板，排查半天才发现是线的问题。

### 🔥 焊接工具（约 $215，也可以先不买）

| 工具 | 型号 | 数量 | 单价 | 在哪买 | 用来干嘛 |
| --- | --- | :-: | --: | --- | --- |
| 电烙铁 | Hakko FX-888DX 恒温焊台（含烙铁架、海绵、清洁丝、T18-D16 刀头） | 1 | $129.95 | [SparkFun](https://www.sparkfun.com/hakko-fx-888dx-soldering-station.html) | 焊排针、焊线 |
| 焊锡丝 | Kester 63/37 含松香芯，0.031"（0.8 mm），1 lb | 1 | $63.23 | [TEquipment](https://www.tequipment.net/Kester/24-6337-0027/Solder-Wire/?b=y) | 63/37 有铅焊锡最好上手，一卷够用好几年 |
| 吸锡带 | Adafruit 1.5 mm × 1.5 m | 1 | $3.50 | [Adafruit #149](https://www.adafruit.com/product/149) | 焊错了把锡吸掉 |
| 助焊剂笔 | Kester 951 | 1 | 约 $10 | DigiKey / Amazon | 让焊锡更好流动，焊点更亮 |
| 护目镜 | 任意 ANSI Z87.1 认证款 | 1 | 约 $8 | 五金店 / Amazon | 剪引脚、焊接时防止东西弹进眼睛 |

> [!NOTE]
> **可以先不买焊接工具**：UW 的 MILL makerspace（CoMotion 管理）有焊台，学生完成安全培训后免费使用（[UW ECE](https://ece.uw.edu/entrepreneurship/makerspace-accelerating-innovation)、[UW 工学院介绍](https://engr.washington.edu/news/article/2019-01-03/meet-the-mill)）。第一批元件到货后，把所有排针一次性去那里焊完，桌面阶段就不需要自己的烙铁了。**未核实**：寒假期间 MILL 的开放时间，以及那里是否提供焊锡等耗材，去之前先查官网或发邮件问。

> [!WARNING]
> 有铅焊锡焊完要洗手，焊的时候开窗或开风扇，不要在吃东西的桌子上焊。

<a id="notice"></a>

## ⚠️ 下单前注意

> [!WARNING]
> - **麦克风 ICS-43434 已被 Adafruit 标为停产**，目前还有库存，建议第一批尽早买；买不到就换 Adafruit SPH0645（#3421，接线和用法基本一样）。
> - **主控板 Adafruit 缺货**时去 DigiKey 或 Mouser 买乐鑫官方的同型号，认准 `ESP32-S3-DevKitC-1-N8R8`，别买成 N16R8V（1.8 V 版本）。
> - **电池接头**：Gens ace 这款默认是 Deans（T 型）接头，买对应的公头，或者换成 XT30 版本，和第 15 项保持一致。
> - **锂电池安全**：只用平衡充电器充电，充电时放防爆袋里、有人看着，鼓包的电池不要再用。

<a id="order"></a>

## 🧾 建议的下单方式

把同一家店的东西凑一单，省运费。每下一单，就把那一行最前面的方块改掉：

| | # | 在哪买 | 买什么 |
| :-: | :-: | --- | --- |
| ⬜ | 1 | **Adafruit** | 麦克风、功放、喇叭、面包板、跳线、USB 线、吸锡带（+ 可选传感器） |
| ⬜ | 2 | **Pololu** | 电机驱动、电机 ×2、编码器线、轮子、万向球、降压模块（编码器线目前缺货，留意到货） |
| ⬜ | 3 | **DigiKey / Mouser** | 主控板（Adafruit 缺货时）、电容、开关、接头、斜口钳、剥线钳、助焊剂笔 |
| ⬜ | 4 | **Waveshare 官网** | 屏幕（从深圳发货，运费和到货时间下单时看，未核实） |
| ⬜ | 5 | **航模店（GetFPV / GensTattu）** | 电池、充电器、防爆袋 |
| ⬜ | 6 | **其他** | 万用表（Home Depot）、焊台（SparkFun）、焊锡（TEquipment） |

<sub>⬜ 没下单 · 🟨 已下单 · ✅ 已到货</sub>

<a id="solder"></a>

## 🪛 哪些要自己焊

大部分小模块到货时排针是散装的，需要焊上才能插面包板。

| 元件 | 要不要焊 | 说明 |
| --- | --- | --- |
| 主控板 ESP32-S3-DevKitC-1 | ✅ 一般不用 | 乐鑫官方开发板通常出厂已焊好排针（产品页没写明，到货确认一下） |
| 麦克风 ICS-43434 | 🔥 要 | 焊排针（Adafruit 页面没写是否附排针，到货确认） |
| 功放 MAX98357A | 🔥 要 | 焊附带的排针；喇叭接口是已焊好的螺丝接线端子 |
| 喇叭 | ✅ 不用焊 | 线头是 JST PH 2 针插头，和功放的螺丝端子对不上，剪掉插头、剥线后拧进端子即可 |
| 屏幕 Waveshare 3.5" | ✅ 一般不用 | 用 15 针接口的排线连接；Waveshare 的屏幕模块一般附带杜邦线排线（到货确认，未核实）。杜邦母头插不进面包板的话，用公对公跳线转接 |
| 电机驱动 TB6612 | 🔥 要 | 焊附带的 1×16 排针 |
| 电机 + 编码器 | 🔥 要 | 编码器线（#4763）一头是插头，另一头是 28 AWG 散线，要焊到排针上才能插面包板。电机电源是否也走这根 6 芯线，Pololu 产品页没写明，未核实 |
| 5 V 降压 D24V50F5 | 🔥 要 | 焊附带的 5 针排针，或者直接焊输入 / 输出线 |
| 电池 | 🔥 要 | 电池是 Deans（T 型）插头，要把对应的公头焊到电源线上 |
| 电容、开关、接头 | 🔥 要 | 装车时焊到电源线上 |
| 陀螺仪 LSM6DSOX（可选） | ✅ 不用 | 用 STEMMA QT 线免焊连接（线要另买，约 $1） |

---

<p align="center"><sub><a href="../docs/PLAN.md">← 📝 开发计划</a> &nbsp;·&nbsp; <a href="README.md">🔌 硬件</a> &nbsp;·&nbsp; <a href="../docs/devlog">🐛 调试记录 →</a></sub></p>
