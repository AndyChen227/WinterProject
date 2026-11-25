# Learning C for Embedded Systems

从零学 C 语言，到能在 ESP32-S3 上用 FreeRTOS 做一台会对话的 AI 电子宠物小车。这个仓库记录全过程：课程笔记、练习代码、刷题和项目。

## 路线

| 阶段 | 时间 | 内容 | 目录 |
| --- | --- | --- | --- |
| 1. C 入门 | 2026.11 – 2026.12 中 | 变量、循环、函数、数组、字符串 | [courses/01-c-basics](courses/01-c-basics) |
| 2. C 进阶 | 寒假第 1 周 | 指针、结构体、动态内存、位运算 | [courses/02-c-advanced](courses/02-c-advanced) |
| 3. ESP32 入门 | 寒假第 1–3 周 | GPIO、中断、PWM、SPI 屏幕、I2S 音频、Wi-Fi | [courses/03-esp32-basics](courses/03-esp32-basics) |
| 4. FreeRTOS | 2027.01 | 任务、队列、信号量、调度 | [courses/04-freertos](courses/04-freertos) |
| 5. 面试准备 | 2027.01 – 03 | 嵌入式常见问题、模电数电、射频基础 | [courses/05-interview-prep](courses/05-interview-prep) |
| 项目 | 寒假 – 春季学期 | AI 电子宠物小车（ESP32-S3 + 大模型） | [projects/ai-pet-car](projects/ai-pet-car) |
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
│   └── ai-pet-car/          # AI 电子宠物小车
└── NOTE_TEMPLATE.md         # 笔记模板
```

## 约定

- 笔记文件名：`01-variables.md`、`02-loops.md`，按学习顺序编号，代码文件同名（`01-variables.c`）。
- 每学完一个知识点，在对应课程 README 里把 `- [ ]` 改成 `- [x]`。
- commit 信息写清楚做了什么，例如 `c-basics: arrays notes + 3 exercises`。

## 学习流程（每看完一节课）

1. **笔记**：复制 `NOTE_TEMPLATE.md` 到对应课程的 `notes/`，按知识点命名，比如 `courses/01-c-basics/notes/03-loops.md`。
2. **代码**：把课上的例子自己敲一遍，再写 1–2 个自己的小练习，放到 `code/`，和笔记同名（`03-loops.c`）。
3. **打勾**：在课程 README 里把学会的知识点 `- [ ]` 改成 `- [x]`。
4. **提交**：`git add . && git commit -m "c-basics: loops notes + 2 exercises" && git push`。
5. **每周日**：更新下面的进度，没学完的写一句卡在哪。

> CS50 的 problem set 答案不要放进这个公开仓库：CS50 的学术诚信政策不允许公开答案。problem set 放在本地或单独的私有仓库，这里只放笔记和自己写的练习。

## 进度

- [ ] C 入门
- [ ] C 进阶
- [ ] ESP32 入门
- [ ] FreeRTOS
- [ ] AI 电子宠物小车
- [ ] LeetCode 50 题
