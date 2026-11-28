<sub>[📚 课程](../README.md) › 01 · C 入门</sub>

<img src="../../projects/ai-pet-car/media/art/mascot-happy.svg" width="90" align="right">

# 📘 01 · C 入门

> 学会 C 的基本语法：变量、循环、函数、数组、字符串。

| 🗓️ 时间 | 🎬 课程 | 🎯 完成标准 |
| --- | --- | --- |
| 2026.11 – 12 中<br>期末期间每天约 1 小时 | Harvard CS50 Week 1–3<br><sub>英文吃力时换翁恺《C 语言程序设计》</sub> | 不看答案能独立写出 20 道简单题 |

## 📒 笔记

| # | 知识点 | 笔记 | 代码 | 日期 | 掌握 |
| :-: | --- | :-: | :-: | :-: | :-: |
| 01 | Hello, C：写、编译、运行 | [📝](notes/01-hello-c.md) | [💾](code/01-hello-c.c) | 11-26 | ★★★☆☆ |
| 02 | 库、变量与输入输出 | [📝](notes/02-input-output.md) | [💾](code/02-input-output.c) | 11-27 | ★★★☆☆ |

## 🎓 对应 CS50

| CS50 | 内容 | 对应下面的知识点 |
| --- | --- | --- |
| Week 1 · C | 类型、条件、循环、`make`/编译 | 环境、基础语法、流程控制 |
| Week 2 · Arrays | 数组、字符串、命令行参数 | 数组与字符串 |
| Week 3 · Algorithms | 查找、排序、递归 | 函数（递归） |

<sub>Week 0（Scratch）可以跳过，你写过 Python/Java。</sub>

## 🧠 知识点

### 环境
- [x] 在命令行编译运行 `hello.c`（用 cs50.dev 网页版，免安装）
- [ ] 理解编译 → 链接 → 运行的过程

### 基础语法
- [ ] 变量与数据类型：`int` `char` `float` `double`，各占多少字节（`sizeof`）
- [ ] 常量、`#define`
- [ ] 输入输出：`printf` / `scanf` 与格式符
- [ ] 运算符：算术、关系、逻辑、自增自减，优先级

### 流程控制
- [ ] `if` / `else`、`switch`
- [ ] `for` / `while` / `do-while`
- [ ] `break` / `continue`

### 函数
- [ ] 定义、声明、调用、返回值
- [ ] 形参与实参（值传递）
- [ ] 局部变量、全局变量、`static`
- [ ] 递归

### 数组与字符串
- [ ] 一维数组、二维数组
- [ ] 数组作为函数参数
- [ ] 字符数组与字符串、`'\0'`
- [ ] 常用字符串函数：`strlen` `strcpy` `strcmp` `strcat`

### 多文件
- [ ] 头文件 `.h` 与源文件 `.c` 的分工
- [ ] `#include` 与头文件保护（`#ifndef`）

## 💪 练习建议

每个知识点写 2–3 个小程序放到 `code/`，例如：温度换算、判断素数、冒泡排序、数组求最大值、字符串反转、九九乘法表。

---

<p align="center"><sub><a href="../README.md">📚 课程总览</a> &nbsp;·&nbsp; <a href="../02-c-advanced">📗 02 · C 进阶 →</a></sub></p>
