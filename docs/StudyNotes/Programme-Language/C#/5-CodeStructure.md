# 5.C#的代码结构

我们在 VS 2022 中新创建的一个 `*C*-*Sharp` 文件（通常是以 `文件名.cs` 的文件形式）的时候，通常会为我们自动补全代码的结构。

结构例子（HelloWorld.cs）：

```csharp
// C# 示例
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HelloWorldCS
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // 你的光标会自动到达这里
        }
    }
}
```

作为一位初学者来说，这样的代码结构很显然是完全看不懂的，不懂为什么需要有 `namespace` 、`internal class ...` 等等…

既然我们不清楚它们的作用在何处，那么我们可以尝试将其删除掉。

删除掉多余结构的例子（HelloWorld.cs）：

```csharp
// C# 示例
class Program
{
    static void Main()
    {
    }
}
```

在我们删除掉多余部分之后，所显现出来的代码结构便是这样子的。

那么它们分别是什么呢？

1. `class` `static` `void` 可以认为它们是 C# 语言当中的关键字之一；
2. `class` 后跟着的是是一个名称 `Program` ，名称可以随意修改；
3. `*Main`* ：指的是一个函数的名称，**但需要注意的是 `*Main` 函数名称在 C# 当中属于关键字之一；***它指的*是一个程序的入口，在程序执行的时候会先从这个函数开始执行后续的代码；*

- <del>ps: 它们 Main 函数写法跟 Java 很像：</del>
    
    ```java
    // Java 示例
    public class Main {
        public static void main() {
        }
    }
    ```
    

因此可以看到，C# 语言中最基本的一个代码结构便是这样子的：

```text
// C# 伪代码示例
类 名称
{
    函数()
    {
        // 代码语句1
        // 代码语句2
        // 代码语句3
        // 代码语句n...
    }
}
```

参考资料：

[**【C#零基础入门教程 Visual Studio 2022】人生低谷来学C# P5：C#代码结构**](https://www.bilibili.com/video/BV1NA4y1R7vL/?p=5)