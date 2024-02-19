# just do it日报

# Just Do It.

## 2024.1.22

今日任务：

- [x] 练字半小时

- [x] 数学大纲

- [x] 洗牙

- [x] csapp重做习题

- [x] cs61a查看网站

- [x] 打字练习20分钟

  <img src="C:\Users\crx\AppData\Roaming\Typora\typora-user-images\image-20240122194408527.png" alt="image-20240122194408527" style="zoom:33%;" />

### `size_t`的用法

补充C基础。

之前一直不是很了解为什么`show_bytes`要用`size_t`作为长度单位，代码实例：

```c
typedef unsigned char *byte_pointer;

void show_bytes(byte_pointer start, size_t len) {
    size_t i;
    for (i = 0; i < len; i++)
	printf(" %.2x", start[i]);    //line:data:show_bytes_printf
    printf("\n");
}
```

然后在《C Primer Plus》中找到了`size_t`的用途。

`sizeof`函数返回的是一个无符号整数，但是并未确定其变量类型。所以不同机器用`sizeof`可能要用unsigned int、unsigned long甚至是unsigned long long类型的变量来存储。

这样会导致的问题首先就是，你想用`printf`打印`sizeof`的表达式，你需要了解自己计算机系统用什么类型数据存储`sizeof`。并且不利于后续的移植开发。

所以C直接定义了一个`sizeof`返回的类型`size_t`，专门用来保存sizeof函数产生的无符号整数变量。此时printf函数使用`z`修饰符表示打印相应的类型。

还是得以权威的工具书为指导啊，查了半天人家几句话就讲明白了。

### 关于Byte Ordering

首先理解最高位字节：一个数据用n位的二进制表示为[wn-1, wn-2, ... , w1,w0]。那么wn-1就是二进制的最高位而w0为最低位。假设n为8的倍数，那么[wn-1, wn-2, ... , wn-8]就是最高位字节。

如果一个系统从数据的最高位字节开始存储（地址从低到高），一直存到数据的最低位字节，那么这个系统就是“大端”存储类型。所以如果想要检测下自己的系统是哪种类型存储数据的，最简单的方法就是按字节输出int类的变量0x12345678。

如果输出结果为12 34 56 78，那么大端存储。如果结果为78 56 34 12，那么小端存储。

## 1.23

今天突然想回去，但是csapp。有没有一种可能，就是csapp并不影响你回去？是的，只需要有电脑就好了。

## 1.25

今日学习下cs61a的课程大纲，了解下课程的培养目标。

然后就是csapp的题目，按照进度安排，这周五做完第二章题目的话，现在还有几个题？

需要做10个题目，才能基本完成这周的计划，这样周末完成第二章大作业。（2.63-2.73）

我觉得不算难，主要是考虑时间别太多，直接看答案解析这一遍，然后再自己考虑解决方法。

### cs61a的课程大纲

We consider a series of techniques for controlling program complexity, such as functional programming, data abstraction, and object-oriented programming.

Homeworks are weekly assignments meant to help you apply the concepts learned in lecture and section on more challenging problems.

The purpose of homework is for you to learn the course material, not to prove that you already know it.（很喜欢的一句话(●'◡'●) ）

**If you are stuck on a problem, come get help instead of copying the answer from someone else or the Internet; you'll still get credit and won't be flagged for cheating**

Problem solving practice is the key to progress in computer science.

### csapp

现在时间来到了下午14:27，现是时候做几个c题目来熟络熟络筋骨了。

ok，第一个2.63就卡了我好久。主要是因为算术右移的那个函数，确定是否执行算术右移的时候出问题了：取得最高位，如果是1则需要执行算术右移（前面补1），否则不需要补1。

```C
int sra(int x, int k) {
    int complement_quantity = sizeof(int) << 3 - k;
    int xsrl = (unsigned) x >> k;

    //get the sign bit :10000... or 000000...
    int sign_bit = (1 << (complement_quantity - 1)) & xsrl;

    //reverse_sign_value:will get 0 if sign_bit != 0
    int reverse_sign_value = !sign_bit - 1;
    
    int mask = -1 << complement_quantity;
    
    return xsrl | reverse_sign_value & mask;
}
```

取得的最高位`sign_bit`并不是一个单独的位，所以根据这个值是否为空来判断是否执行补1操作的话，需要利用逻辑操作和-1的奇思妙想。

挺有意思，我一开始想用`!!sign_bit`的方法得到是否跟mask进行或操作，当`sign_bit`为0，则`!!sign_bit`值为0；当`sign_bit`不为0，则`!!sign_bit`值为1。这样跟mask操作也不是很方便，所以才想到了-1的操作。

现在已经17：12分了，仅做第一个题，有点挫败的。

ok，现在吃了老妈做的木耳芹菜山药炒肉后，满血复活了。

在做两个题目，现在遇到一个题目超级有意思，虽然以我现在的能力解决不了，但是将答案研究一遍还是能做到的。

上题目：

![image-20240125184322375](C:\Users\28075\AppData\Roaming\Typora\typora-user-images\image-20240125184322375.png)

题目的梗概就是：用书中的规则（不能用循环、判断等），写一个函数，入参一个x。当x的二进制表示中1的数量为奇数个，则函数返回1，否则返回0。

这里我想循环计数1的想法被规则打破了：不能用循环和条件判断。

在我反复确认无法以现阶段的能力解决后，我决定看答案，研究他们是怎么解决这个炙手山芋的。上代码：

```C
int odd_ones(unsigned x){
    x ^= x >> 16;
    x ^= x >> 8;
    x ^= x >> 4;
    x ^= x >> 2;
    x ^= x >>1;
    x &= 0x1;
    return x;
}
```

牛逼，当时觉得这代码真tm优雅，几行就解决问题了，这能行？

研究完以后，真牛逼，这能行！

他巧妙地用异或操作，将整个数的奇偶性逐渐控制到了最低位。第一次，作为一个32位的数据，右移16位后与原数据做异或操作。高16位和低16位作异或操作，这样会导致低16位数据中成对的1消失。

而消失掉重复1后的低16位数据，保留了原32位数据的奇偶性（虽然数量不一致，但是只要整体的奇偶性不变就可以）。

这样重复执行下去，就会让低8、4、2、1位保留原32位的奇偶性，最终原数据的奇偶性就会体现在最低位上。

所以这个题目，就没使用统计数量，而是用的异或的性质：同类相消，将影响奇偶的份子去除掉。最终实现了获取整个数据的奇偶性。

## 1.26

今日早起练字，很不错的开局。今天是鸭旺口集，一会去买点水果。

现在就是将cs61a的lab研究一下。

需要买的东西：

- [ ] 插排收纳

按照cs61a的手册完成了第一节课的环境布置。下午写一下csapp第二章的homework（某些题目真的挺难，但是为了变得更强，请just do it！）

今天真牛逼，做了5个题目，做到了2.70。准备睡觉了。

## 1.27

cs61a：

When stuck on a problem, try to explain the area in which you are stuck.

Do the readings before lecture! (but what should i read?slide or oneline book?)

When preparing for the midterms and final, do past exam questions! Lecture, lab, and discussion provide a great introduction to the material, but the only way to learn how to solve exam-level problems is to do exam-level problems.

ok，发现了2024年春季新版的cs61a，而且是两周前开的课，直接跟进新课程的进度。

好吧，现在发现需要用到python编写函数的语法，可是我不会~需要补一下知识了。

## 1.28

昨天下午给小伙子开了一下午家长会，听了海川中学的宣讲，感觉这个学校是办正事的，不知道小伙子中考能去哪里？

今天开始cs61a的课本教材，然后到10点左右坐车去万虹广场跟大家聚一下。

[1.2  Elements of Programming](https://www.composingprograms.com/pages/12-elements-of-programming.html)里面对于代码的可读性阐释：A programming language is more than just a means for instructing a computer to perform tasks. The language also serves as a framework within which we organize our ideas about computational processes. Programs serve to communicate those ideas among the members of a programming community. Thus, programs must be written for people to read, and only incidentally for machines to execute.

代码作为交流思想的工具，不仅仅只是指挥电脑实现具体功能，而且是思想传递的媒介。所以代码不仅仅需要能跑起来，而且需要读得懂。

## 1.29

昨天孙某韦某见面会，回来帅总亲切让我们滚。

今天回顾昨天的知识：

python函数相对于数学中缀表达式的三个优点：

1. 函数可以有任意个参数（因为数学公式中参数一旦多起来，就很难去得到这个表达式的原本意图）
2. 函数可以任意嵌套
3. 函数免去了各种奇怪上下标、公式符号的限制，简单明了。

今天学的知识：

引用库的方法：from modules import functions，等以后对于python的语法了解清晰后，可以用官方文档[python3Library](https://docs.python.org/3/library/index.html)来寻找自己想要的函数。

赋值语句居然是一个简单的抽象，它将等号右边复杂的表达式，与左边的简单变量名联系起来，我们可以直接用简单变量名（类似于area），就可以获取对应复杂操作的值（retrieving those values by name）。赋值语句在右边表达式计算尚未完成之前，是不能跟左边变量名进行连接的。所以py的交换两个数的值可以用一个函数

跑步完毕，回来做饭。

下午csapp。

## 1.30

早晨起来后，先过了一遍csapp的课后题目。

现在记录下2.70的题目：

```C
// Write code for the function with the following prototype:
/*
* Return 1 when x can be represented as an n-bit, 2’s-complement
* number; 0 otherwise
* Assume 1 <= n <= w
*/
int fits_bits(int x, int n);
```

对于这个题目，需要思考下步骤。

题目要求：如果这个数据能被n位的二进制补码表示，则返回1。

一个int类型的数怎么才能被n位的二进制补码表示呢？

举例1，x = [001001]，能否被n = 4的二进制补码表示？不能，因为n = 4的时第4位为符号位，如果此时数据的第四位恰好为1，则4位的二进制补码数据则会与原数据值不相同。

举例2，x = [001001]，能否被n = 3的二进制补码表示？不能，因为3位的二进制补码肯定不能正确展示原长度为4的数据。

在这里定义一下原数据的最高位1的位置为w。想用n位的二进制补码正确表示原数据，就需要n >= 1 + w;

但是这里并不能用判断，这就需要从另一个角度去考虑。

如果这个数据能被n位的二进制补码表示，那么它跟原数据有什么关联吗？

1. 原数据 == 被二进制补码表示的数据（n > w）
2. 原数据左移(32 - n)位，然后再算术右移（32 - n）位，原数据不变。（这样就包括了第一步的判断相等的问题）

代码：

```C
#include <stdio.h>
#include <assert.h>
/*
* Return 1 when x can be represented as an n-bit, 2’s-complement
* number; 0 otherwise
* Assume 1 <= n <= w
*/
int fits_bits(int x, int n){
  int w = sizeof(int) << 3;
  return x == (x << (w - n) >> (w - n));
}
int main(){
  assert(fits_bits(0x1234, 16));
  assert(!fits_bits(0x90, 8));
  assert(fits_bits(0x90, 9));
  assert(!fits_bits(0x7F, 7));
  assert(fits_bits(0x7F, 8));
  return 0;
}
```

明天赶集了，今天能稍微赶赶进度吗？

csapp这几道题，难度真的不低，这都是第三次做了，还是用了我两个小时（我期待1h以内就能完成的）。

然后卡我的时间较多的地方简单在这做下记录：

1. 边界问题：获取第k位的数据（x & (1 << (k - 1))）
2. 题型见的少，没有思路：像是能否用n位的二进制补码表示这个数据（只能是多做多思考😉 ）

ok，开始cs61a的道路，今天看看能否将`1.3  Defining New Functions`和`1.4  Designing Functions`看完并且理解了。别着急，多轮重复起来。

函数名称（起名的艺术）

1. 函数名都是小写字母，单词之间要以下划线分隔，起描述性的函数名
2. 参数名要有意义（《代码整洁之道》）

函数定义要隐藏细节。能做到下一个人在调用你写的函数的时候，只关心函数的描述而不用关心函数的操作。

函数抽象的三个属性：

1. 定义域（范围）：能够使用的函数参数
2. 值域：函数的返回值集合
3. 意图：输入与输出的联系

现在学习cs61a遇到的问题：文档中对于专业名词和长难句运用较多，阅读起来速度较慢。感觉这个问题一时半会也解决不了，需要慢慢积累吧。

函数设计时的规则（同《代码整洁之道》）

1. 每一个函数都应该仅做一项任务
2. 不要重复自己
3. 函数应该具有一般性（实现乘方而不仅仅是平方）

Remember, code is written only once, but often read many times. 哈哈哈，太担心辣鸡代码了。

## 1.31

今日赶集，买了80块的苹果，我们比卖苹果的人都先到了集上，所以好吃的苹果都被我们买过来了。

今天继续cs61a，重新回顾下昨天学习的知识。

函数中的返回表达式仅仅在调用此函数的时候才会被计算。

计算表达式的环境中，包含了许多连续的栈帧。An `import` statement binds a name to a built-in function. A `def` statement binds a name to a user-defined function created by the definition.

今天看了下课程安排，![image-20240131160030163](C:\Users\28075\AppData\Roaming\Typora\typora-user-images\image-20240131160030163.png)

如果说这周到2.2号完成的话，需要解决ch1.6的文章和几个lab。

这周cs61a任务就是完成1.6章节的阅读，然后做题。但是还有一个问题就是，我的csapp进度呢？

现在做到了2.70题目，还有30道题。

## 2.1

今日任务：

- [ ] 阅读cs61a的1.6和1.7节文章
- [ ] 做5个csaqq题目（2.71-2.75）

今天在偶然阅读python的蟒蛇书时候，发现了作者写的几句话：

> 这里，我建议大家：
>
> 1. 第一部分尽可能在42小时内快速浏览一遍（2天之内），不用理解，先混个眼熟
> 2. 第二部分跟着项目实践精读，对应查阅第一部分的基础知识点，针对性地自我解答。
>
> 这样你就能从枯燥的语法、控制结构、数据结构等无穷的编程概念中挣脱出来，进入一个具体真实的项目场景中，一切将变得异常清晰、有目标且可检验。

这里我再去检视自己的学习方法：

1. 想将阅读材料全部掌握（不符合学习逻辑，应该是用到什么，再深入理解地去学什么。应该以问题驱动学习，而不是单纯学习不去应用知识）
2. 阅读英文文章的时候，会有走神的现象（语法卡住后，自己的精神就会恍惚一下🥲）

其实就是想死磕英语语法，为了语法而去阅读，但是忘记了英语只是一个工具，能读懂就行了。

现在就可以这样，先通篇略读，第一遍看看代码执行逻辑，然后第二遍看看概念介绍，第三遍再通读一遍。这段时间尽量控制在1h以内。好的，开始实践，预计8：40应该可以将第6节过一遍。（其实难度主要在这个文档的长难句语法上，可能也需要我耐心阅读来积累长难句的语法）

ok，现在是8：32，读到了1/3的部分，时间去哪了？

在读的时候，对设计模式产生了兴趣（因为这个函数的抽象实在是太牛逼了）

```py
>>> def improve(update, close, guess=1):
        while not close(guess):
            guess = update(guess)
        return guess
```

然后下载大话设计模式pdf，在往cs文件夹移动的时候，就发现了 [健康学习到150岁 - 人体系统调优不完全指南](https://github.com/zijie0/HumanSystemOptimization)这个当时摘录的文章，然后就走神进去了一会...

额，一个小时应该可以浏览完这个文章了，不走神的前提下，现在起身锻炼下身体，然后再8：45分开始到10点，解决1.6章节学习。

下午过来报道：

cs61a的阅读材1.6章节料现在已经读了3/5了，很牛逼。因为里面既有新知识：函数作为参数调用时的一些特性，原谅我现在想不起来上午的知识点了，一会再回顾一下吧。

现在就练习下打字速度，然后投入到csapp的学习当中。今天1.6和1.7应该是可以完结的，加油！

csapp的2.72题目

```C
/* Copy integer into buffer if space is available */
/* WARNING: The following code is buggy */
void copy_int(int val, void *buf, int maxbytes) {
if (maxbytes-sizeof(val) >= 0)
	memcpy(buf, (void *) &val, sizeof(val));
}
```

这个代码中的判断逻辑：`maxbytes-sizeof(val) >= 0`会导致这个题目出现“即使maxbytes < sizeof(val)也会执行复制操作”。

因为函数`sizeof()`会返回一个无符号数，而maxbytes是有符号数，这样运算的时候，就会导致类型转换。而类型转换在表达式的时候，如果一个操作数是有符号整数，而另一个是无符号整数，那么有符号整数会被转换为无符号整数。

这样就可以解释为什么出现“即使maxbytes < sizeof(val)也会执行复制操作”的问题了：两者转为无符号整数运算后，数据永远大于等于0，导致这个判断条件永远为真。

所以修改策略也很简单，就是强制将`sizeof()`返回的值转换为统一的有符号类型数据再处理。

## 2.2

今天稳步向前就好，别急功近利了。

### 2.74

这里挂一下csapp的2.74问题和答案，进行分析，学到了赋值的新思路。

> **Write a function with the following prototype:**
>
> ```C
> /* Determine whether arguments can be subtracted without overflow */
> 
> 	int tsub_ok(int x, int y);
> ```
>
> **This function should return 1 if the computation x-y does not overflow**

首先这个题目并没有要求使用164页的编程规则限制，也就是说你其实可以用条件判断和循环来实现这个题目。然后另一个问题就是，怎么样才能更简单实现这个功能。

我的思考肯定是基于这两个判断表达式的：

```C
if(x < 0 && y > 0 && sub > 0) return 0; //负溢出
if(x > 0 && y < 0 && sub < 0) return 0; //正溢出
```

然后可以看看答案是怎么考虑这个问题的，之所以记录这个题目，就是因为这个题目运用了逻辑运算与`&&`的短路特性来使得代码简化了（随之而来的是可读性变差的结果）：

```C
/*
 * tsub-ok.c
 */
#include <stdio.h>
#include <assert.h>
#include <limits.h>

/* Determine whether arguments can be substracted without overflow */
int tsub_ok(int x, int y)
{
    int res = 1;
    /* 如果y为INT_MIN，则x为任意值都会溢出：
    x > 0,sub < 0; 
    x < 0(x此时取值范围为 [INT_MIN,0) ),sub >= 0--突然发现这个条件是判断是否溢出的一个定理，可以重点记忆一下
    */
    (y == INT_MIN) && (res = 0);
    // if (y == INT_MIN) res = 0;

    /*这里就是很正常的条件判断，但是利用了逻辑与 && 运算符的短路特性*/
    int sub = x - y;
    int pos_over = x > 0 && y < 0 && sub < 0;
    int neg_over = x < 0 && y > 0 && sub > 0;

    res = res && !(pos_over || neg_over);

    return res;
}

int main(int argc, char* argv[]) {
  assert(!tsub_ok(0x00, INT_MIN));
  assert(tsub_ok(0x00, 0x00));
  return 0;
}
```

可以看到这个题目中，用到了逻辑运算与 `&&` 运算符的短路特性来判断是否溢出了。用chatgpt来分析这个` (y == INT_MIN) && (res = 0);`语句实现了什么功能，可以得到答案：

> 这个表达式使用了逻辑与 `&&` 运算符，它具有短路特性。表达式中有两部分：
>
> 1. `(y == INT_MIN)`：检查变量 `y` 是否等于 `INT_MIN`，即判断 `y` 是否为整型最小值。
> 2. `(res = 0)`：将变量 `res` 赋值为 `0`。
>
> 这两部分由 `&&` 连接在一起，整个表达式的结果取决于两部分的值。
>
> 如果第一部分 `(y == INT_MIN)` 为真（即 `y` 等于 `INT_MIN`），那么第二部分 `(res = 0)` 也会被执行。这是因为在逻辑与运算中，如果第一个条件为真，那么第二个条件就会被检查并执行。在这种情况下，整个表达式的值为真。
>
> 如果第一部分 `(y == INT_MIN)` 为假，那么第二部分 `(res = 0)` 将不会被执行，因为短路特性会导致整个表达式的值为假。
>
> 这样的表达式通常用于条件赋值的场景。如果 `y` 的值等于 `INT_MIN`，则将 `res` 的值设置为 `0`；否则，保持 `res` 的原始值。在实际编码中，这种写法可能会让代码可读性变差，应该慎用。最好将条件判断和赋值操作分开，以提高代码的清晰度。

那么其实这个题目用了某种取巧的方法简化了代码结构，其实可读性变差了。但是仍然加强了对于逻辑运算符的理解。

其实2.74还蕴藏着一个知识点：两个数的和什么时候会溢出。

当x + y > TMAX，或者x + y < TMIN时，这时候就会导致溢出。若根据这两个判断条件来确定当溢出时x和y的范围，则需要分类讨论：

1. x > 0时，因为TMIN < y < TMAX，所以x + y > TMIN + x是永远不会负溢出的。但是可能会出现x+ y > TMAX的正溢出的场景。此时x > 0，那么y的取值范围就是(TMAX - x, TMAX]
2. x < 0时，x + y = TMAX + x永远不会正溢出。但是会出现负溢出（x + y < TMIN）的场景。y的取值范围是[TMIN, TMIN - x)

### 2.73

然后再看2.73这个题目：

> Write code for a function with the following prototype:
>
> ```C
> /* Addition that saturates to TMin or TMax */
> 	int saturating_add(int x, int y);
> ```
>
> Instead of overflowing the way normal two’s-complement addition does, saturating
> addition returns TMax when there would be positive overflow, and TMin
> when there would be negative overflow. Saturating arithmetic is commonly used
> in programs that perform digital signal processing.
>
> Your function should follow the bit-level integer coding rules (page 164).

当程序运算有溢出的时候，返回对应的边界值（TMIN，TMAX），并且不能用判断循环等。看下答案怎么处理的这个情况：

```C
/*
 * saturating-add.c
 */
#include <stdio.h>
#include <assert.h>
#include <limits.h>

int saturating_add(int x, int y) {
  int sum = x + y;
  int sig_mask = INT_MIN;//0x80000000
  /*
   * if x > 0, y > 0 but sum < 0, it's a positive overflow
   * if x < 0, y < 0 but sum >= 0, it's a negetive overflow
   */
  int pos_over = !(x & sig_mask) && !(y & sig_mask) && (sum & sig_mask);
  int neg_over = (x & sig_mask) && (y & sig_mask) && !(sum & sig_mask);

  (pos_over && (sum = INT_MAX) || neg_over && (sum = INT_MIN));

  return sum;
}

int main(int argc, char* argv[]) {
  assert(INT_MAX == saturating_add(INT_MAX, 0x1234));
  assert(INT_MIN == saturating_add(INT_MIN, -0x1234));
  assert(0x11 + 0x22 == saturating_add(0x11, 0x22));
  return 0;
}
```

这里有两个问题需要研究代码解决：

1. 在没有条件判断符的情况下，如何判定正负溢出？
2. 溢出后，怎么确定正负溢出然后返回对应的边界值？

首先分析在没有关系运算符的情况下，此函数如何判断正溢出的：

```C
  int pos_over = !(x & sig_mask) && !(y & sig_mask) && (sum & sig_mask);
```

当x & sig_mask == 0 ，y & sig_mask == 0且sum & sig_mask != 0的时候，这个正溢出标志pos_over等于1成立。下面逐一分析正溢出的这几个条件：

`x & sig_mask == 0`：只要x的最高位为0即可，这样对应的x的取值就去除了负数部分，此时x的取值范围为：`x >= 0`。

`y & sig_mask == 0`：同理，y的最高位为0，y的取值范围为`y >= 0`。

`sum & sig_mask != 0`:此时证明参数sum的最高位一定为1，此时sum的取值范围为：`sum < 0`

所以结合注释，可以得到问题1的答案。由原来需要关系运算符（>和<）`if x > 0, y > 0 but sum < 0, it's a positive overflow`，到现在直接利用二进制补码的特性——即最高位是否为1，和逻辑运算符`&&`的短路特性，来判断x、y和sum是正数还是负数，从而得到相同的溢出判断结果。

既然正溢出可以用逻辑运算与`&&`和位运算符`&`来获得，那么负溢出的分析也是相同的，这里就不再赘述。

然后就是分析`溢出后，怎么确定正负溢出然后返回对应的边界值`的问题。这里放下答案中对于这个问题处理的代码：

```C
(pos_over && (sum = INT_MAX) || neg_over && (sum = INT_MIN));
```

这里还是利用了逻辑运算与`&&`的短路特性：如果正溢出，则执行`sum = INT_MAX`；如果负溢出，则执行`sum = INT_MIN`。

截至今天下午16：49分，研究完毕两个题目，现在需要慢下脚步来考虑下下一步该怎么走。

### 职业规划

java应该是不想走了，我想往底层发展，而且我现在学的这些东西，都是为了以后能更好地在计算机底层方面大放光彩的。

那就选择C++和python。现在粘贴一张BOSS直聘上关于c++招聘的一些技能要求，然后看看该怎么发展：

第一个，编译器开发工程师：

<img src="C:\Users\28075\AppData\Roaming\Typora\typora-user-images\image-20240202165334019.png" alt="image-20240202165334019" style="zoom:50%;" />

```
我们诚招对计算机体系结构和计算机系统（Computer Systems & Architecture）熟悉的研发工程师与我们团队中一群才华横溢的工程师一起工作，为未来的异构计算平台开发世界一流的计算机系统。
基本要求
● 计算机科学、自动化、电子与信息、数学等理工类相关专业本科及以上学历
● 全职、兼职或者实习（实习至少半年）
● 具有较强的责任心和学习能力，工作态度积极，敢于迎接挑战
职责描述
● 参与操作系统、编译器、计算库和相关软件的设计和实现
● 分析和开发基准测试和测试应用程序
● 配合产品部门进行产品的调度和计划
● 设计文档、测试文档及其他相关文档的编写和维护
技能和经验
● 精通 C/C++ 编程，有较强的算法和数据结构基础
● 熟悉计算机体系结构、操作系统和编译优化
● 熟悉并行计算和高性能计算
● 精通开发、测试、交付和维护生产质量的软件
● 拥有开源软件开发经验、为开源项目做过贡献以及与开源社区有合作经验者优先
● Computer Systems & Architecture 以及 Compiler 领域硕士或博士学位者优先
```

技能要求：

1. 精通 C/C++ 编程，学明白C++
2. 较强的算法和数据结构基础，需要学习ds
3. 熟悉计算机体系结构、操作系统和编译优化，这个在完成cs61a，csapp，以及对应的计算机组成、操作系统（pa）等对应课程后即可完成。
4. 熟悉并行计算和高性能计算--待研究
5. 拥有开源软件开发经验、为开源项目做过贡献以及与开源社区有合作经验者优先--在github上是否贡献过自己的力量。

另一个C++开发的例子：语音合成引擎开发工程师

<img src="C:\Users\28075\AppData\Roaming\Typora\typora-user-images\image-20240202170323254.png" alt="image-20240202170323254" style="zoom:50%;" />

技能要求：

1. 3年以上c++/c语言开发经验，好吧，算我熟悉？
2. 熟悉基本数据结构，基础功底扎实。同上文数据结构
3. 有构建大型c++软件的经验，熟练掌握设计模式--设计模式
4. 熟悉CPU体系结构，对ARM或者X86 CPU/ Register/Cache/Memory/Bus有较深入理解，会针对硬件特性就关键计算瓶颈做分析--同计算机底层结构分析
5. 熟悉ARM neon/X86 AVX2/512 指令集，有过使用SIMD指令做具体算法优化的经验。--还是熟悉的指令集调用者，PA！

再次确认下自己今年的学习路线吧。

## 2.3

本周任务：

1. 收尾工作：做完2.75和cs61a的1.6和1.7章节
2. 周报总结
3. 找一个合适的离线音乐播放器（暂定为椒盐音乐）

## 2.4

昨日与徐某艺术馆一游，遇见学妹校友。

今天：

- [x] 回顾2.73和2.74题目
- [ ] 新做2.75题目（不会就立刻研究答案，并且写下思路）
- [ ] 研究originOS4的新用法
- [x] 研究vivo个人模式
- [x] 研究离线音乐相关问题，并且将歌单音乐导入其中
- [x] 将手机及其原始照片数据切换至vivo+切换移动资费
- [x] 关闭apple的在线服务（仍保存云空间）

为了更好地消费时间，现在采用番茄todo25分钟计数，然后放松5分钟回顾下自己到底学到了什么。

第一个番茄时钟结束，完成2.74和2.73的题目重写，这里再具体研究下逻辑运算符。

回顾2.74题目，发现在最后返回是否溢出的时候，两个溢出标志用了逻辑运算符`||`：

```c
  res = res && !(pos_over || neg_over);
```

在这分析下这句话的作用：

首先是括号内的`pos_over || neg_over`，这里的意思是：当正溢出或者负溢出时候，此条件成立。即只要是溢出了，则此括号内的运算结果为1。

那此时`!(pos_over || neg_over)`就相当于一个mask：若计算结果溢出，则返回0；若不溢出，则返回1。

那我有个疑问，这个mask就是一个根据是否正溢出或者负溢出而判断溢出的标志掩码，那么我能否在括号内将`||`换为`&&`？

那此时只要有一个溢出标志为假，那么这个mask的取值就会成为：若两边都溢出，则返回0；若其中有一个溢出或者都不溢出，则返回1。这样与题目的要求不符合：只要溢出，则返回0。

所以这个`||`不能换为`&&`。

第二个番茄时钟完成，完成上文分析。

在做75题目的时候，发现课后习题是跟课文内容强关联的。所以我觉得后期优化csapp学习的方法就是，先快速浏览一遍内容，尽量按照习题去过基础内容。

75题目是关于补码和无符号整数的乘法运算，这里重新回顾下之前的无符号和补码的乘法运算。

比较重要的是：补码的乘法结果 = 无符号数的乘法结果取模后再转换为补码形式的结果。

发现不会做，直接看答案：

```C
/*
 * unsigned-high-prod.c
 */
#include <stdio.h>
#include <assert.h>
#include <inttypes.h>

int signed_high_prod(int x, int y) {
  int64_t mul = (int64_t) x * y;
  return mul >> 32;
}

unsigned unsigned_high_prod(unsigned x, unsigned y) {
  /* TODO calculations */
  int sig_x = x >> 31;
  int sig_y = y >> 31;
  int signed_prod = signed_high_prod(x, y);
  return signed_prod + x * sig_y + y * sig_x;
}

/* a theorically correct version to test unsigned_high_prod func */
unsigned another_unsigned_high_prod(unsigned x, unsigned y) {
  uint64_t mul = (uint64_t) x * y;
  return mul >> 32;
}

int main(int argc, char* argv[]) {
  unsigned x = 0x12345678;
  unsigned y = 0xFFFFFFFF;

  assert(another_unsigned_high_prod(x, y) == unsigned_high_prod(x, y));
  return 0;
}
```

看代码的时候，发现有人评论：

![image-20240204152211555](C:\Users\28075\AppData\Roaming\Typora\typora-user-images\image-20240204152211555.png)

> can I ask one question?
> why `int64_t mul = (int64_t) x * y;`must here explicit cast then implicit cast?(I thought I have seen related contents in csapp, but search "explicit" found nothing related)

额，为什么在x * y的时候强制类型转换为64位的。这里蕴含着两个问题：

1. 这个强制类型转换做了什么操作
2. 为什么要做这个操作

其实我现在知道的是x和y的补码乘积会溢出（例如x = INT_MIN、y = INT_MIN时，x*y的结果会超出32位的范围），溢出后计算机会自动将其高32位去除，保留低32位。这样也等效于结果取2的32次方的模。

所以需要将其计算结果转为64位，然后才能保存乘法运算中溢出的高位数据。

但是这个`(int64_t) x*y`，是先将x和y转为64位后（等价于`(int64_t) x * (int64_t) y`）再运算呢还是将计算结果（等价于`(int64_t)x*y`）转为64位呢？我不了解，因为我不清楚乘法运算符和类型转换符号的先后顺序，以及能否在得到结果后再强制类型转换。

那就首先解决这个类型转换和乘除法的优先级问题。

在菜鸟教程[C 强制类型转换](https://www.runoob.com/cprogramming/c-type-casting.html)中，示例代码非常贴合现在我们遇到的问题：

```C
#include <stdio.h>
 
int main()
{
   int sum = 17, count = 5;
   double mean;
 
   mean = (double) sum / count;
   printf("Value of mean : %f\n", mean );
 
}
```

下面对这个代码的解释也很到位：

> 这里要注意的是强制类型转换运算符的优先级大于除法，因此 **sum** 的值首先被转换为 **double** 型，然后除以 count，得到一个类型为 double 的值。

关于强制类型转换和乘除法的运算优先级，查询chat-gpt：

> 由于 `x` 被强制类型转换为 `int64_t`，整个表达式会采用更宽的整数类型（`int64_t`）进行计算，因此 `y` 会隐式地升级到 `int64_t`，避免了整数溢出的问题。

其实这样就解决了这个问题的两个疑惑：

1. 这个强制类型转换做了什么操作？

   答：将参数`x`的类型转换为 `int64_t`。

2. 为什么要做这个操作？

   答：想让x和y的乘积不溢出。这需要让结果类型为64位，这样就需要将两个参数进行升级。

   但是现在可以利用C语言的类型升级（涉及两种类型的运算，两个值会被分别转换成两种类型的更高级别）来简化代码书写规则：只需要将其中一个参数x升级为64位的类型，另一个低级类型参数y在参与运算的过程中会被自动转换为64位的数据。

   这样两个64位的数据得到的结果是64位的数据，正好可以保存32位int类的乘法溢出的高位数据，解决了溢出问题。

## 2.5

今天主要任务是cs61a的项目，学到了关于debug的相关问题和lab1的一些题目，感觉挺简单的。

但是lab1的debug可以再看看，还有课本也可以再回顾下（卡好时间，不会就查

## 2.6

今天意识到昨天没怎么记录自己的所做的事情。今天就从第一个番茄todo开始，记录自己的时间使用情况。

首先继续cs61a的课程计划。下面写下本周待办清单

- [x] 30mins对比[Lab1答案](https://cs61a.org/lab/sol-lab00/)（15分钟即可搞定）
- [ ] 1h重读cs61a课本关于1-7节的内容
- [ ] [ Disc 01: Control, Environment Diagrams](https://cs61a.org/disc/disc01/)
- [ ] [Hog](https://cs61a.org/proj/hog/)
- [ ] [HW 02: Higher-Order Functions](https://cs61a.org/hw/hw02/)
- [ ] [Lab 02: Higher-Order Functions, Lambda Expressions](https://cs61a.org/lab/lab02/)
- [ ] [Disc 02: Environment Diagrams, Higher-Order Functions](https://cs61a.org/disc/disc02/)
- [x] 研究2.75题目
- [ ] csapp2.76-2.80
- [ ] 确认c++学习路线

对比Lab1答案，关于Q3: Falling Factorial

> ### Q3: Falling Factorial
>
> Let's write a function `falling`, which is a "falling" factorial that takes two arguments, `n` and `k`, and returns the product of `k` consecutive numbers, starting from `n` and working downwards. When `k` is 0, the function should return 1.
>
> ```python
> def falling(n, k):
>     """Compute the falling factorial of n to depth k.
> 
>     >>> falling(6, 3)  # 6 * 5 * 4
>     120
>     >>> falling(4, 3)  # 4 * 3 * 2
>     24
>     >>> falling(4, 1)  # 4
>     4
>     >>> falling(4, 0)
>     1
>     """
>     "*** YOUR CODE HERE ***"
> ```

官方提供的算法很简单：

```python
def falling(n, k):
	total, stop = 1, n-k #设置边界stop
    while n > stop:
        total, n = total*n, n-1
    return total
```

对比lab1的答案已经在第一个番茄时钟内完成。下两个番茄时钟主要是略读一遍cs61a的课本，因为接下来的项目需要用到里面更多的内容。

因为阅读原英文手册极其费劲（会注意力涣散），所以我搜了搜如何让自己英语阅读速度更快：[如何提高英文阅读速度？](https://www.zhihu.com/question/19559519)

重新学习课本，整理以下知识点：

1. 为什么称为变量？因为在程序执行的不同时段，名称可以跟不同的值进行绑定：In Python, names are often called *variable names* or *variables* because they can be bound to different values in the course of executing a program.

2. 利用py会优先执行赋值语句等号右边的表达式，所以交换值很方便：With multiple assignment, *all* expressions to the right of `=` are evaluated before *any* names to the left are bound to those values. As a result of this rule, swapping the values bound to two names can be performed in a single statement.

   ```python
   >>> x, y = 3, 4.5
   >>> y, x = x, y
   >>> x
   4.5
   >>> y
   3
   ```

3. print作为“非纯函数”的代表，除了返回一个`None`外，还会产生额外输出

   ```py
   >>> print(print(1), print(2))
   1
   2
   None None
   ```

4. Both `def` statements and assignment statements bind names to values, and any existing bindings are lost.

   ```py
   >>> def g():
           return 1
   >>> g()
   1
   >>> g = 2
   >>> g
   2
   >>> def g(h, i):
           return h + i
   >>> g(1, 2)
   3
   ```

5. The return expression is not evaluated right away; it is stored as part of the newly defined function and evaluated only when the function is eventually applied.

6. An `import` statement binds a name to a built-in function. A `def` statement binds a name to a user-defined function created by the definition. 

7. Applying a user-defined function introduces a second *local* frame, which is only accessible to that function.The environment in which the body is evaluated consists of two frames: first the local frame that contains formal parameter bindings, then the global frame that contains everything else.

8. The body of a function is not executed until the function is called (not when it is defined).

9. In *environment* ,each function is a line that starts with `func`, followed by the function name and formal parameters.

10. *scope*:We say that the *scope* of a local name is limited to the body of the user-defined function that defines it.

11. abstractions in functions:A programmer should not need to know how the function is implemented in order to use it. 

ok，截止到下午2点31分，重读完了1-3节。然后跑了10km。

回来研究2.75，发现被函数`unsigned_high_prod(x, y)`卡住：

```C
unsigned unsigned_high_prod(unsigned x, unsigned y) {
  /* TODO calculations */
  int sig_x = x >> 31;
  int sig_y = y >> 31;
  int signed_prod = signed_high_prod(x, y);
  return signed_prod + x * sig_y + y * sig_x;
}
```

这里翻译一下最终的结果：无符号乘积的高32位 = 对应有符号乘积的高32位 + x * y的符号位 + y * x的符号位。

这里涉及到有符号和无符号数的乘法规则：

<img src="C:\Users\28075\AppData\Roaming\Typora\typora-user-images\image-20240206191327119.png" alt="image-20240206191327119" style="zoom:50%;" />

## 2.7

今天继续本周目标。但是需要注意提升效率，因为没有ddl，所以做起事情来没有目标并且速度很慢。

其实真正学习知识慢一点完全没问题，但是像是英语阅读速度就是制约前进的巨大阻碍。

所以我今天在《刻意练习》这本书中找一下关于“如何提升英语阅读水平”的相关灵感。![image](https://s3.cn-north-1.amazonaws.com.cn/assets.xmind.cn/uploads/img/ff9569217a1586a5850a28b1661599f2.png)

把《刻意练习》下载到kindle里，很感兴趣作者是怎么举例的。

查询了下，现在对于英文阅读能力的要求是每分钟400个单词。

现在回到[如何提高英文阅读速度？](https://www.zhihu.com/question/19559519/answer/380807713
)，这里面介绍了四个提升英语阅读速度的方法：

1.  避免默读：对于阅读理解来说，你只需要看到文字并理解字面意思即可，不需要知道它的读音。如何解决默读问题？**关键还是要靠你的意识，你要在脑海里刻意地不断提醒自己不要去想它的发音。**
2. 意群阅读：将句子结构抽象为一个个的块，而不是一个个孤立的单词。**解决了默读的问题，我们已经能确保停顿的时间都花在获取字面信息上，所以接下来要提高的就是每次停顿获取的信息量。**如果每次凝视只能看到一个单词的话，你获取信息的效率就太低了，而你应当看到的是一个短语、词组、一部分信息，也就是我们说的意群。意群的快速划分需要大量阅读的积累。掌握的意群阅读的原理后，在阅读的过程中要不断尝试扩大每次凝视的宽度，从而在单位时间内获取更多的信息。
3. 主动阅读：要精准阅读，带着问题去读
4. 语法：主谓

总结一下训练方法：

1. 停止默读单词
2. 组块阅读而不是每个单词的阅读
3. 带着问题去阅读
4. 大量阅读英语文章重复训练上述三个能力

现在是9点半，半小时看看能否用以上三个能力去重新阅读完cs61a的第3节。（可以）

**Name Evaluation.** A name evaluates to the value bound to that name in the earliest frame of the current environment in which that name is found.

Tests typically take the form of another function that contains one or more sample calls to the function being tested.

现在花了28分钟看完了1.5章节，但是很困。下午跑完了10km，因为在1.6节遇到了困难：

1. 牛顿法不了解
2. 嵌套程序不熟悉
3. currying法不熟悉

这几个问题导致我现在难以进行下去，明天先把这几个概念和程序写一遍，然后再去阅读材料。

明天可以加入一篇外刊阅读，卡时间读完，锻炼英语阅读的速度。

## 2.8

ok，今天主要任务就是将1.6节涉及到的概念弄明白，然后再通读一遍。如果有余力，那么请将2.75和csapp进度继续推进。

今天可以看下关于微积分的学习。

首先是了解牛顿方法：[Newton's method](https://amsi.org.au/ESA_Senior_Years/SeniorTopic3/3j/3j_2content_2.html)

了解完毕，继续看1.6，这次先把里面涉及的代码跑一遍去理解下，然后再通读一遍。

## 2.9

昨天下午直接帮忙干活（帮忙吃东西）

今天继续1.6。

1. An important feature of lexically scoped programming languages is that locally defined functions maintain their parent environment when they are returned. 

## 2.10

新年快乐，祝你新的一年Be open and go beyond yourself !

## 2.11

今天要去姥爷家玩了。

去之前看看材料。

## 2.13

ok，昨天郑兆乐来玩的，玩了玩双人成行，放松一下。

今天学习学习hog。

## 2.14

昨天跟姑姑姑父聊了下学习方面的问题，期待两位小伙子的成绩。

今天主要是去国栋大哥家站站，聊聊天。

继续hog项目。然后今天阅读下《丹尼尔斯的跑步训练》，为今年的马拉松做准备。除此以外，确定下今年的阅读书单，博客园开一个书单栏目，准备今年的阅读。

另外为了督促自己的学习，也在博客园开自己的cs61a和csapp的学习记录。

csapp的学习以梳理知识点，记录一些课后作业（有意思的题目）为主。

cs61a的话，因为有很多课后作业，暂且将自己的学习记录贴上吧，等以后再考虑具体创作方向。

今天就是打开博客园，开三个栏目，讲述自己以后想在每个模块想做的事情。

![image-20240214181052403](C:\Users\28075\AppData\Roaming\Typora\typora-user-images\image-20240214181052403.png)

## 2.15

上午完成hog规则部分的全部内容。

现在搞一下让我一直头疼的csapp2.75问题。

2.75题目描述

> Suppose we want to compute the complete 2w-bit representation of x . y, where
> both x and y are unsigned, on a machine for which data type
>
> unsigned is w bits.
> The low-order w bits of the product can be computed with the expression x*y, so
> we only require a procedure with prototype
>
> ```C
> unsigned unsigned_high_prod(unsigned x, unsigned y);
> ```
>
> that computes the high-order w bits of `x*y` for unsigned variables.
> We have access to a library function with prototype
>
> ```C
> int signed_high_prod(int x, int y);
> ```
>
> that computes the high-order w bits of x . y for the case where x and y are in two’scomplement
> form. Write code calling this procedure to implement.
>
> the function
> for unsigned arguments. Justify the correctness of your solution.
>
> **Hint**: Look at the relationship between the signed product x . y and the unsigned
> product x
>  . y
>  in the derivation of Equation 2.18.

等式2.18为：
$$
(x'.y') mod 2^\omega =
[(x + x_{\omega-1}.2^\omega).(y + y_{\omega-1}.2^\omega)]mod2^\omega
\\= [x.y+(x_{\omega-1}.y+y_{\omega-1}.x)2^\omega+x_{\omega-1}y_{\omega-1}2^{2\omega}]
\\=(x.y)mod 2^\omega
$$
这个问题抽象为程序语言的话，就是：

> 乘法得出的2w位数据被保存在2w位变量`unsigned_prd`中，
>
> 分别再用w位的变量`unsigned_high_bits`和`unsigned_low_bits`，分别去保存变量`unsigned_prd`的高w位和低w位。

协助完成这个保留无符号数乘法结果高w位的方法，是对应有符号数保留高w位的方法`signed_high_prod`。

我们需要找到有符号数高w位和无符号数高w位之间的关系，因为我们已经知道无符号数乘法和有符号数乘法最终结果的二进制表示是一致的，而最终结果就是乘法的结果对`2^w`求模运算得来的。

假设不截断无符号整数的乘法结果（2w位）：`unsigned_prd = ux * uy` 

那么截断为低w位的结果为：`unsigned_low_bits = unsigned_prd mod 2^w`.

这样乘法结果的高w位数据就可以得出：`unsigned_high_bits =  (unsigned_prd - unsigned_low_bits ) mod 2^w`

这里需要强调下，`unsigned_prd`是2w位的无符号变量，而保存其高、低w位的无符号变量`unsigned_high_bits`和`unsigned_low_bits`均为w位数据。

同理也可以得到有符号数的高低w位数据，其实公式都相同，只是把unsigned改为signed。

上述分析结束，就可以利用公式去推导下“如何利用有符号数乘法的高w位去表示无符号数的高w位”，我这里想用markdown自带的公式写的，寻思这样更清晰一些，但是上面等式2.18敲完了我就打了退堂鼓--因为语法太麻烦了！

这样我就在这贴一下自己手写的推导公式：<img src="C:\Users\28075\Desktop\17079823282211707982166990.jpg" alt="2.75solution" style="zoom:50%;" />

这样再去理解代码就方便很多了。贴一下[2.75答案](https://dreamanddead.github.io/CSAPP-3e-Solutions/chapter2/2.75/)

```C
/*
 * unsigned-high-prod.c
 */
#include <stdio.h>
#include <assert.h>
#include <inttypes.h>

int signed_high_prod(int x, int y) {
  int64_t mul = (int64_t) x * y;
  return mul >> 32;
}

unsigned unsigned_high_prod(unsigned x, unsigned y) {
  /* TODO calculations */
  int sig_x = x >> 31;
  int sig_y = y >> 31;
  int signed_prod = signed_high_prod(x, y);
  return signed_prod + x * sig_y + y * sig_x;
}

/* a theorically correct version to test unsigned_high_prod func */
unsigned another_unsigned_high_prod(unsigned x, unsigned y) {
  uint64_t mul = (uint64_t) x * y;
  return mul >> 32;
}

int main(int argc, char* argv[]) {
  unsigned x = 0x12345678;
  unsigned y = 0xFFFFFFFF;

  assert(another_unsigned_high_prod(x, y) == unsigned_high_prod(x, y));
  return 0;
}
```

欢迎讨论csapp的相关问题~😉

## 2.16

今日：

- [x] 2h cs61a
- [x] 阅读1h
- [ ] csapp 2h

还有比较重要的是，我下一步的学习和生活道路是什么。

## 2.17

昨日烦恼的超哥来到了这里，祝愿兄弟能一切顺利吧。

hog的项目来到了问题8。

## 2.18

早起跑步10km，跑到水闸附近有股鱼腥味。

## 2.19

在写`def make_averaged(original_function, samples_count=1000):`函数的时候，发现函数很容易实现，但是加入实际的情景就没法理解。现在在这里记录下自己遇到的问题：

### Problem 8 (2 pt)问题描述	

> Implement `make_averaged`, which is a higher-order function that takes a function `original_function` as an argument.
>
> The return value of `make_averaged` is a function that takes in the same number of arguments as `original_function`. When we call this returned function on the arguments, it will return the average value of repeatedly calling `original_function` on the arguments passed in.
>
> Specifically, this function should call `original_function` a total of `samples_count` times and return the average of the results of these calls.

### 问题解析

这个问题其实很简单。`make_averaged`函数接受两个参数：

1. `original_function`：接受n个参数，返回一个值
2. `samples_count`：重复调用函数A的次数

接受了两个入参后，返回一个函数（高阶函数，将函数作为返回值）。这个函数接受的参数与`original_function`接受的参数相同。调用这个新函数的时候，会返回重复调用`samples_count`次`original_function`的值。

### 疑问

但是在检测自己是否理解这个函数（`python3 ok -q 08 -u`）的选项中，对于这个问题我总是答错：

```python
>>> from hog import *
>>> dice = make_test_dice(3, 1, 5, 6)
>>> averaged_roll_dice = make_averaged(roll_dice, 1000)
>>> # Average of calling roll_dice 1000 times
>>> # Enter a float (e.g. 1.0) instead of an integer
>>> averaged_roll_dice(2, dice)
?
```

在我理解中，`dice`被定义好后，每次调用`dice`就会指定下一个值，然后循环如此。（这个坑好久之前就被埋好了😒 ）

`roll_dice`呢，就是一个函数，接收投掷总数和骰子类型，返回投多个骰子的总点数（遵循sow sad原则）。

那么既然说这个`make_averaged`函数是重复调用`samples_count`次`original_function`的值，那么就先看看在这里调用一次`original_function`的效果，然后看看重复调用`samples_count`的效果。

1. `roll_dice(2, dice)`：这个函数就是`make_averaged`参数1。这个函数投掷两次骰子，然后算总和。例如第一次投掷两枚骰子，结果分别为3和1，符合“sow sad”原则，所以这次结果为1。
2. 重复调用`samples_count`次的结果：这就是我卡住的地方，也是需要反思的地方。

### 解决思路

这里因为我并没有深入理解`dice`函数的机制，导致我并不理解重复调用`dice`到底有什么效果。下面贴上`dice`的代码，学习一下嵌套函数如何利用`nonlocal`将修改上一层函数的变量:

```py
def make_test_dice(*outcomes):
    """Return a die that cycles deterministically through OUTCOMES.

    >>> dice = make_test_dice(1, 2, 3)
    >>> dice()
    1
    >>> dice()
    2
    >>> dice()
    3
    >>> dice()
    1
    >>> dice()
    2

    This function uses Python syntax/techniques not yet covered in this course.
    The best way to understand it is by reading the documentation and examples.
    """
    assert len(outcomes) > 0, 'You must supply outcomes to make_test_dice'
    for o in outcomes:
        assert type(o) == int and o >= 1, 'Outcome is not a positive integer'
    index = len(outcomes) - 1
    def dice():
        nonlocal index
        index = (index + 1) % len(outcomes)
        return outcomes[index]
    return dice
```

这里的`dice()`函数中，使用`nonlocal index`的声明，`dice()`可以修改`make_test_dice`的局部变量`index`。

这样代码就好理解了：

```py
>>> dice = make_test_dice(3, 1, 5, 6)
```

`dice`每次调用的时候，都会改变`make_test_dice`的局部变量`index`。这样`index`就会循环往复地在`[0, len(outcomes) - 1]`中徘徊。

使用 `nonlocal` 关键字可以指示 Python 解释器在嵌套函数中查找并修改上一层函数的局部变量。

这样再去看`roll_dice(2, dice)`重复调用`samples_count`次的结果：第一次投掷两个骰子，结果分别为3和1，得分为1；第二次投掷两个骰子，结果分别为5和6，得分为11；第三次投掷两个骰子，结果分别为3和1，得分为1...

这样重复调用的结果就是1和11，重复1000次的平均值就是（1 * 500 +11 * 500） / 1000  = 6.0。

### 总结

1. 请读源码：调用函数解决问题前，需要详细理解每一个函数到底做了什么。
2. 遇到问题：那肯定是你代码没弄明白又或者是出现了bug，请再次重新回顾代码，做到详尽理解和测试。
3. 偷懒被教育：`nonlocal`关键字懒得查，注释` This function uses Python syntax/techniques not yet covered in this course.
       The best way to understand it is by reading the documentation and examples.`也懒得理解，最终导致了让我跌了个跟头。而这个坑又是自信的我亲手埋下的。
