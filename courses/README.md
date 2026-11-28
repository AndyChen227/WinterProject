<sub>[🏠 首页](../README.md) › 📚 课程</sub>

<img src="../projects/ai-pet-car/media/art/mascot-happy.svg" width="90" align="right">

# 📚 课程

> 五门课，从第一行 `hello, world` 到嵌入式面试。

<img src="assets/roadmap.svg" alt="课程路线：C 入门 → C 进阶 → ESP32 入门 → FreeRTOS → 面试准备" width="100%">

## 🗺️ 现在学到哪了

| | 课程 | 时间 | 学完能做什么 | 笔记 | 状态 |
| :-: | --- | --- | --- | :-: | :-: |
| 📘 | [**01 · C 入门**](01-c-basics) | 2026.11 – 12 中 | 不看答案独立写出 20 道简单题 | 2 | 🟨 |
| 📗 | [**02 · C 进阶**](02-c-advanced) | 寒假第 1 周 | 用指针写单链表，用位运算操作某一位 | 0 | ⬜ |
| 🔌 | [**03 · ESP32 入门**](03-esp32-basics) | 寒假第 1–3 周 | 屏幕显示表情，电机前进后退转圈 | 0 | ⬜ |
| ⚙️ | [**04 · FreeRTOS**](04-freertos) | 2027.01 | 小车代码拆成多个任务，用队列传指令 | 0 | ⬜ |
| 💼 | [**05 · 面试准备**](05-interview-prep) | 2027.01 – 03 | 每个常见问题能用中文讲 1–2 分钟 | 0 | ⬜ |

<sub>⬜ 没开始 · 🟨 进行中 · ✅ 完成</sub>

<a id="flow"></a>

## 🔁 每学完一个知识点

| | 步骤 | 做什么 |
| :-: | --- | --- |
| 📝 | **1.&nbsp;笔记** | 复制 [`NOTE_TEMPLATE.md`](NOTE_TEMPLATE.md) 到对应课程的 `notes/`，按知识点命名<br><sub>例如 `courses/01-c-basics/notes/03-loops.md`</sub> |
| ⌨️ | **2.&nbsp;代码** | 把课上的例子自己敲一遍，再写 1–2 个自己的小练习<br><sub>放进 `code/`，和笔记同名（`03-loops.c`）</sub> |
| ✅ | **3.&nbsp;打勾** | 在课程 README 里把学会的知识点 `- [ ]` 改成 `- [x]`，笔记表加一行 |
| 🚀 | **4.&nbsp;提交** | `git add . && git commit -m "c-basics: loops notes + 2 exercises" && git push` |

> [!IMPORTANT]
> CS50 的 problem set 答案**不要**放进这个公开仓库，这里只放笔记和自己写的练习。

## 📁 每门课长这样

```
01-c-basics/
├── README.md          # 这门课的首页：笔记列表 + 知识点清单
├── notes/
│   └── 01-hello-c.md  # 笔记：编号-知识点.md
└── code/
    └── 01-hello-c.c   # 代码：和笔记同名
```

---

<p align="center"><sub><a href="../README.md">← 🏠 首页</a> &nbsp;·&nbsp; <a href="01-c-basics">📘 01 · C 入门 →</a></sub></p>
