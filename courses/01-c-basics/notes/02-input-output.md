<sub>[🏠 首页](../../../README.md) › [📚 课程](../../README.md) › [📘 01 · C 入门](../README.md) › 笔记</sub>

# 02 · 库、变量与输入输出

`🗓️ 2026-11-27` · `🎬 CS50 Week 1` · `★★★☆☆` · [`💾 02-input-output.c`](../code/02-input-output.c)

> [!NOTE]
> **一句话**：库是别人写好的函数，`#include` 之后就能用；用户输入的东西装进**带类型的变量**里，再用 `printf` 的占位符打印出来。

## 🧠 要点

**1. 库（library）= 别人写好、可以直接用的一堆函数。**

| 头文件 | 里面有什么 | 来源 |
| --- | --- | --- |
| `stdio.h` | 输入输出：`printf` | C 自带 |
| `string.h` | 处理字符串：`strlen` | C 自带 |
| `math.h` | 数学：`sqrt`、`pow` | C 自带 |
| `cs50.h` | 读取输入：`get_string`、`get_int`，还有 `string` 类型 | CS50 课程专用 |

**2. 头文件（`.h`）是库的「目录」。** 里面是函数的**声明**，只说怎么用，不写怎么实现：

```c
int get_int(string prompt);
// 返回类型  函数名  (参数)
```

真正的代码在另一个编译好的文件里，编译的最后一步会把它**链接**进来。不写 `#include`，编译器就不认识这个函数。

**3. 变量 = 带类型的盒子。** 写法是 `类型 名字 = 值;`，**从右往左读**：

```c
string answer = get_string("what's your name? ");
```

先调用 `get_string`（括号里是**参数**）→ 用户输入后它交回一个**返回值** → `=` 把它装进叫 `answer` 的盒子。`=` 是**赋值**，不是「等于」。和 Python 不同，C 必须写出变量的类型。

**4. 类型、读取函数、占位符是配套的。**

| 类型 | 装什么 | 读取 | 占位符 | 大小 <sub>cs50.dev</sub> |
| --- | --- | --- | :-: | :-: |
| `char` | 一个字符 `'y'` | `get_char` | `%c` | 1 字节 |
| `int` | 整数，最大约 21 亿 | `get_int` | `%i` | 4 字节 |
| `long` | 更大的整数 | `get_long` | `%li` | 8 字节 |
| `float` | 小数 | `get_float` | `%f` | 4 字节 |
| `double` | 更精确的小数 | `get_double` | `%f` | 8 字节 |
| `string` | 一串文字 `"Chan"` | `get_string` | `%s` | |

**5. `printf` 按顺序把值填进占位符。**

```c
printf("%s is %i years old\n", name, age);
```

第一个占位符 `%s` 配第一个值 `name`，第二个 `%i` 配 `age`，数量和顺序都要对上。

## 💻 代码

```c
#include <cs50.h>   // get_string、get_int、string 类型
#include <stdio.h>  // printf

int main(void)
{
    string name = get_string("What's your pet's name? ");
    int age = get_int("How old is it? ");

    printf("%s is %i years old\n", name, age);
}
```

```
$ ./02-input-output
What's your pet's name? Cora
How old is it? 3
Cora is 3 years old
```

## 🐛 容易踩的坑

| 现象 | 原因 | 怎么改 |
| --- | --- | --- |
| 编译器说不认识 `string` 或 `get_string` | 忘了 `#include <cs50.h>` | 在文件开头加上 |
| `error: format specifies type 'int' but the argument has type ...` | 占位符和值的类型对不上，比如 `%i` 配了一个 `string` | 对照上面的表，类型和占位符要配套 |
| 算出来的数变成奇怪的负数 | 结果超过了 `int` 的上限（约 21 亿） | 换成 `long` 和 `%li` |

## 🔌 嵌入式里怎么用

- 芯片上没有键盘，也没有 `cs50.h`。`#include` 的会换成芯片厂商的库，比如 ESP-IDF 的 `driver/gpio.h`，用法一样：包含头文件，然后调用函数。
- 类型的大小**跟着芯片变**：`long` 在 cs50.dev 上是 8 字节，在 ESP32 上只有 4 字节。所以嵌入式代码常用 `stdint.h` 里写明位数的类型，比如 `uint8_t`、`int32_t`。

## ✅ 自测

<details>
<summary>❓ <code>string answer = get_string("name? ");</code> 这一行做了哪几件事？</summary>

1. 调用 `get_string`，把提示语 `"name? "` 作为参数传进去
2. 函数打印提示语，等用户输入，再把输入的文字作为返回值交回来
3. 声明一个 `string` 类型的变量 `answer`
4. `=` 把返回值装进 `answer`

</details>

<details>
<summary>❓ 头文件（.h）里放的是什么？为什么要 #include？</summary>

放的是函数的**声明**（返回类型、函数名、参数），还有类型定义和常量，**不包含**函数的具体实现。`#include` 之后编译器才知道这个函数存在、该怎么调用；真正的代码在编译的链接阶段才加进来。

</details>

---

<p align="center"><sub><a href="../README.md">↩ 回到 📘 01 · C 入门</a></sub></p>
