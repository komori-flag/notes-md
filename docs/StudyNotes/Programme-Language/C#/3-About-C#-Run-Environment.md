# 3. 关于C#的运行环境

继续上一节的第一个 C# 程序：

1.newCSharp.cs

```csharp
// 在此处我们就可以编写 C# 的代码了

// 举个例子，先不用看懂
using System;

namespace MySpace
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            Console.ReadKey();
        }
    }
}
```

在我们编写完成以上 C# 程序后也就需要来运行一下来检验我们的成果了吧！

可惜的是计算机看不懂它们，这就像是让只会使用中文的人们去看阿拉伯语等类似。

因此，我们需要一个中间者来翻译我们的话语给到计算机，而这个中间者就是 **编译器** 。

在此引用微软关于 **.NET** 文档的一段话：

![](./img/3-CSRunningEnvironment/image1.png)


C# 是属于 **.NET**（全称叫 **dotNet**，可不叫 点Net 哦）**平台**的一部分，那么其代码的执行势必跟 .NET 平台有关。

- .NET 常用的平台有三种：
    1. .NET Framework：最初的 .NET 平台，仅支持 Windows 的系统；
    2. Mono：为了使在 .NET Framework 上开发的 C# 代码也可以在其它平台（例如：安卓、IOS、Linux 等）运行，由 Miguel de Icaza 牵头创立的跨平台实现。
    3. .NET (Core)：微软主导下，由 .NET 开源基金会创立的跨平台实现，可在多个平台运行。

**这个教程写的多数代码将会使用 .NET Framework 平台来编译运行。**

<del>ps:实际情况下使用其它平台运行也没关系</del>

- 参考资料：
    1. [**【C#零基础入门教程 Visual Studio 2022】人生低谷来学C# P5：C#代码结构**](https://www.bilibili.com/video/BV1NA4y1R7vL/?p=5)
    2. [[.NET平台的历史与发展](https://www.cnblogs.com/shanyou/p/10925141.html)](https://www.cnblogs.com/shanyou/p/10925141.html)