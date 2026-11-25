# Learning C for Embedded Systems

从零学 C 语言，到能在 STM32 上用 FreeRTOS 做一个机械臂。这个仓库记录全过程：课程笔记、练习代码、刷题和项目。

## 路线

| 阶段 | 时间 | 内容 | 目录 |
| --- | --- | --- | --- |
| 1. C 入门 | 2026.11 – 2026.12 中 | 变量、循环、函数、数组、字符串 | [courses/01-c-basics](courses/01-c-basics) |
| 2. C 进阶 | 寒假第 1 周 | 指针、结构体、动态内存、位运算 | [courses/02-c-advanced](courses/02-c-advanced) |
| 3. STM32 入门 | 寒假第 2–3 周 | GPIO、中断、UART、定时器 PWM、ADC、I2C | [courses/03-stm32-basics](courses/03-stm32-basics) |
| 4. FreeRTOS | 2027.01 | 任务、队列、信号量、调度 | [courses/04-freertos](courses/04-freertos) |
| 5. 面试准备 | 2027.01 – 03 | 嵌入式常见问题、模电数电、射频基础 | [courses/05-interview-prep](courses/05-interview-prep) |
| 项目 | 寒假 – 2027.02 | STM32 + FreeRTOS 4 自由度机械臂 | [projects/stm32-robot-arm](projects/stm32-robot-arm) |
| 刷题 | 全程，每天 1 题 | LeetCode（用 C 写） | [leetcode](leetcode) |

## 目录结构

```
.
├── courses/                 # 每门课一个文件夹
│   └── 0X-<course>/
│       ├── README.md        # 大纲 + 知识点清单（学完打勾）
│       ├── notes/           # 笔记，一个知识点一个 .md
│       └── code/            # 练习代码，一个知识点一个 .c
├── leetcode/                # 刷题，文件名：<题号>-<题目英文名>.c
├── projects/
│   └── stm32-robot-arm/     # 机械臂项目
└── NOTE_TEMPLATE.md         # 笔记模板
```

## 约定

- 笔记文件名：`01-variables.md`、`02-loops.md`，按学习顺序编号，代码文件同名（`01-variables.c`）。
- 每学完一个知识点，在对应课程 README 里把 `- [ ]` 改成 `- [x]`。
- commit 信息写清楚做了什么，例如 `c-basics: arrays notes + 3 exercises`。

## 进度

- [ ] C 入门
- [ ] C 进阶
- [ ] STM32 入门
- [ ] FreeRTOS
- [ ] 机械臂项目
- [ ] LeetCode 50 题
