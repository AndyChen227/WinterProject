// 02 · 库、变量与输入输出：问两个问题，再把答案填进一句话里
// 编译：make 02-input-output      运行：./02-input-output
// 注意：用到了 cs50.h，要在 cs50.dev 里编译

#include <cs50.h>   // get_string、get_int、string 类型
#include <stdio.h>  // printf

int main(void)
{
    // 类型 变量名 = 函数(提示语);  从右往左读：先问，再把回答装进盒子
    string name = get_string("What's your pet's name? ");
    int age = get_int("How old is it? ");

    // %s 等一个字符串，%i 等一个整数，按顺序和后面的参数一一对应
    printf("%s is %i years old\n", name, age);
}
