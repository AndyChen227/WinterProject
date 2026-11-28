<sub>[🏠 首页](../../../README.md) › [📚 课程](../../README.md) › [📘 01 · C 入门](../README.md) › 笔记</sub>

# 01 · Hello, C：写、编译、运行

`🗓️ 2026-11-26` · `🎬 CS50 Week 1` · `★★★☆☆` · [`💾 01-hello-c.c`](../code/01-hello-c.c)

> [!NOTE]
> **一句话**：C 代码电脑看不懂，要先用编译器翻译成机器码才能运行，所以每次都是 **写 → 保存 → `make` → 运行**。

## 🧠 要点

**1. 源代码和程序是两个文件。** `hello.c` 是给人看的菜谱，`hello` 是做好的菜。改了菜谱要重新做一遍，才能尝到新味道。

**2. 三条命令走完全程。**

| 命令 | 作用 |
| --- | --- |
| `code hello.c` | 用编辑器打开（不存在就新建）`hello.c` |
| `make hello` | **编译**：把 `hello.c` 翻译成程序 `hello`。没有任何输出就是成功 |
| `./hello` | **运行**：`.` 是当前文件夹，`./hello` 就是运行这里的 `hello` |

<sub>顺手记两个：`clear` 清屏，`ls` 看当前文件夹里有什么。</sub>

**3. 一个 C 程序长这样。**

| 代码 | 意思 |
| --- | --- |
| `#include <stdio.h>` | 借来 `stdio` 这个库，里面有 `printf`。类似 Python 的 `import` |
| `int main(void)` | 程序永远从 `main` 开始执行。`int` 是结束时交回一个整数，`void` 是不需要输入 |
| `{ }` | 框住 `main` 里要做的事，相当于 Python 的缩进 |
| `printf("...");` | 把双引号里的字打印到屏幕上 |
| `\n` | 换行。没有它，终端的 `$` 会紧贴在输出后面 |
| `;` | 一句话说完了。每条语句都要以它结尾 |

**4. 注释有两种**：`// 单行` 和 `/* 多行 */`，编译器会忽略，是写给人看的。

**5. 报错先看第一条。** `hello.c:5:29: error: ...` 的意思是「`hello.c` 第 5 行第 29 个字符出错」，后面的错误常常是第一条连带出来的。

## 💻 代码

```c
#include <stdio.h>  // 借来 printf 这个工具

int main(void)  // 程序永远从 main 开始执行
{
    printf("hello, world\n");  // 打印一行字，\n 是换行
}
```

## 🐛 踩过的坑

| 现象 | 原因 | 怎么改 |
| --- | --- | --- |
| `error: unexpected character <U+FF1B>` | 分号打成了**中文的「；」**，C 只认英文的 `;` | 写代码时切到英文输入法 |
| `error: unknown type name 'h'` | 想在终端打字，光标却还在编辑器里，代码里多了一个 `h` | 打字前先看光标在哪闪 |
| 橙色提示 `hello.c has changed` | 改了代码**没重新 `make`** 就运行，跑的还是旧程序 | 改完一定先 `make` 再 `./hello` |
| `make` 失败后 `./hello` 照样能跑 | 编译失败时不会生成新程序，运行的是上一次成功的旧版本 | 先把报错改完，直到 `make` 没有输出 |
| 输出是 `hello, world$` | 漏了 `\n`，没换行 | 在引号里的结尾加上 `\n` |
| 页面显示 Rebuilding codespace | cs50.dev 闲置约 30 分钟会自动关机，回来时在重启 | 等几分钟，文件不会丢 |

## 🔌 嵌入式里怎么用

流程一模一样，只是多了一步「烧进芯片」。在 ESP32 上是：写 `.c` → `idf.py build`（编译）→ `idf.py flash`（烧录）→ `idf.py monitor`（看输出）。芯片没有屏幕，`printf` 的内容会从串口传回电脑显示。

## ✅ 自测

<details>
<summary>❓ 改了 hello.c 之后直接运行 ./hello，会看到什么？为什么？</summary>

看到的还是**旧的**输出。`./hello` 运行的是上次编译出来的程序，源代码改了不会自动更新它，必须重新 `make hello`。

</details>

<details>
<summary>❓ 编译器是做什么的？源代码和可执行文件有什么区别？</summary>

编译器把人写的**源代码**（文本，`hello.c`）翻译成 CPU 能直接执行的**机器码**（二进制，`hello`）。源代码给人读和修改，可执行文件给机器运行。

</details>

---

<p align="center"><sub><a href="../README.md">↩ 回到 📘 01 · C 入门</a></sub></p>
