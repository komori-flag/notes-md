# async函数
一：[JS异步终极解决方案](#mdjump_01)
二：[async 函数概述](#mdjump_02)
三：[基本用法](#mdjump_03)
四：[语法](#mdjump_04)
> 1. [返回 Promise 对象](#mdjump_04-01)
> 2. [Promise 对象的状态变化](#mdjump_04-02)
> 3. [await命令](#mdjump_04-03)
> 4. [错误处理](#mdjump_04-04)
> 5. [注意事项](#mdjump_04-05)

五：[async 函数的实现原理](#mdjump_05)

---
## <span id="mdjump_01">一：JS异步终极解决方案</span>
由于 JavaSccript 属于单线程语言，所以需要使用到异步编程来加快它的代码执行效率。

异步操作是 JavaScript 编程的麻烦事之一，麻烦到一直有人提出各种各样的方案，试图解决这个问题。

从最早的回调函数，到 Promise 对象，再到 Generator 函数，每次都有所改进，但又让人觉得不彻底。它们都有额外的复杂性，都需要理解抽象的底层运行机制。

异步I/O不就是读取一个文件吗，干嘛要搞得这么复杂？异步编程的最高境界，就是根本不用关心它是不是异步。

async 函数就是隧道尽头的亮光，很多人认为它是异步操作的终极解决方案。

---
## <span id="mdjump_02">二：async 函数概述</span>
<font color=red> async </font>是 ES7 开始才有的与异步操作有关的函数，和 Promise ， Generator 有很大关联的。

可以说，<span id=mdjump_injump_1>async 是 Generator 的<font color=blue>语法糖*</font></span>。

做个对比：
1. Generator函数实现按顺序读取文件
```javascript
// Generator函数实现按顺序读取文件
// 1.txt{1} , 2.txt{2}
// 引入文件管理模块
const fs = require("fs"),

    // 读取文件
    read_File = function (fn) {
        return new Promise(function (res, rej) {
            fs.readFile(fn, "utf-8", (err, data) => {
                err === "null" ? rej(err) : res(data);
            });
        });
    },

    // Generator函数实现按顺序执行读取文件
    gen = function* () {
        yield read_File("./1.txt");
        yield read_File("./2.txt");
    },
    newback = gen();

// 执行操作
newback.next().value.then(data => console.log(data), err => console.log(err));
newback.next().value.then(data => console.log(data), err => console.log(err));
// 1
// 2
```

2. async函数实现按顺序读取文件
```javascript
    // async函数实现按顺序执行读取文件
    asyncRF = async function () {
        let s1 = await read_File("./1.txt"),
            s2 = await read_File("./2.txt");
        return s1 + "、" + s2;
    };

asyncRF().then(data => console.log(data), err => console.log(err));
// 1、2
```

一比较就会发现，async 函数就是将 Generator 函数的星号（*）替换成 async ，将 yield 替换成 await ，仅此而已。

async 函数对 Generator 函数的改进，体现在以下四点：
1. 内置执行器
    <details>
    <summary>展开查看</summary>
    <pre>
    Generator 函数的执行必须靠执行器，
    所以才有了co模块，而 async 函数自带执行器。
    <code>
    let foo = async function(){await 1};
    foo();
    </code></pre>
    </details>

2. 更好的语义
    <details>
    <summary>展开查看</summary>
    <pre>
    async 和 await ，比起 星号 和 yield ，语义更清楚了。
    <font color=red>async 表示函数里有异步操作</font>；
    <font color=red>await 表示紧跟在后面的表达式需要等待结果</font>。
    </pre>
    </details>

3. 更广的适用性
    <details>
    <summary>展开查看</summary>
    <pre>
    co模块约定，yield命令后面只能是 Thunk 函数或 Promise 对象，
    而async函数的await命令后面，可以是 Promise 对象和原始类型的值。
    （数值、字符串和布尔值，但这时会自动转成立即 resolved 的 Promise 对象）
    </pre>
    </details>

4. 返回值是 Promise
    <details>
    <summary>展开查看</summary>
    <pre>
    async 函数的返回值是 Promise 对象，这比 Generator 函数的返回值是 Iterator 对象方便多了。
    你可以用 then 方法指定下一步的操作。
    </pre>
    </details>

进一步说，async函数完全可以看作多个异步操作，包装成的一个 Promise 对象，而await命令就是内部then命令的语法糖。

**补充：**
> 1. 语法糖：也译为糖衣语法，使用它能够增加程序的可读性，从而减少程序代码出错的机会。
> 2. 语法盐：为容易犯错的语法/变量规则中加上的额外语法限制，以避免不良代码的产生，但可能会违背它的初衷，使得代码可读性下降或损害代码质量。

---
## <span id="mdjump_03">三：基本用法</span>
async 函数返回一个 Promise 对象，可以使用 then 方法添加回调函数。

当函数执行的时候，<font color=red>一旦遇到 await 关键字就会先返回，等到异步操作完成，再接着执行函数体内后面的语句</font>。

```javascript
function timeout(ms) {
    return new Promise((resolve) => {
        setTimeout(resolve, ms); // 2.等待此句执行完成
    });
}

async function asyncPrint(value, ms) {
    await timeout(ms); // 1.执行到此先返回一个 Promise
    console.log(value); // 3.执行此句
}

asyncPrint('hello world', 1000);
// 隔了1s之后
// hello world
```

由于 async 函数返回的是 Promise 对象，而这也可以作为 await 命令的参数。

```javascript
async function timeout() {
    await new Promise(function(resolve){
        setTimeout(resolve, 2000); // 2.等待此句执行完成
    }); // 1.立即返回一个promise对象
}

async function asyncfun() {
    await timeout(); // 3.等待调用函数的异步操作执行完成后，继续执行下面的操作
    console.log("Hello World！"); // 4.输出
}
asyncfun();
```

---
## <span id="mdjump_04">四：语法</span>
### 1.<span id=mdjump_04-01>返回 Promise 对象</span>
async 函数在调用时会返回一个 Promise 对象，<font color=red>函数内部的 return 语句返回的值，会成为 then 方法的回调函数参数</font>。

```javascript
async function f() {
    return "Hello World！";
}
f().then(data => console.log(data));
// "Hello World！"
```

当 async 函数抛出错误时，会导致返回的 Promise 对象变为 reject 状态，进而<font color=red>错误对象会被 catch 方法回调函数接收到</font>。

```javascript
async function f() {
    throw new Error("错误");
}
f()
    .then(data => console.log(data))
    .catch(err => console.log(err));
// rejrct Error: 错误
```

### 2.<span id="mdjump_04-02"> Promise 对象的状态变化</span>
<font color=red> async 函数返回的 Promise 对象，必须等到内部所有 await 命令后面的 Promise 对象执行完，才会发生状态改变，除非遇到 return 语句或者抛出错误</font>

```javascript
function promise() {
    return new Promise((resolve) => {
        setTimeout(resolve, 2000);
    });
}
async function f() {
    await promise();
    await promise();
    return "执行完成"; 
}
f()
    .then(data => console.log(data))
    .catch(err => console.log(err));
// （经过了4秒后）"执行完成"
```

### 3.<span id="mdjump_04-03"> await 命令</span>
正常情况下，<font color=red> await 命令后面是一个 Promise 对象。如果不是，会被转成一个立即 resolve 的 Promise 对象</font>

```javascript
async function f() {
    return await "输出";
}
f().then(data => console.log(data));
// "输出"
```

 await 命令后面的 Promise 对象如果变为 reject 状态，则<font color=red> reject 的参数会被 catch 方法的回调函数接收到</font>。

```javascript
async function f() {
    await Promise.reject("错误");
}

f()
    .then(data => console.log(data))
    .catch(err => console.log(err)); // "错误"
```

<font color=red>只要一个 await 语句后面的 Promise 变为 reject ，那么整个 async 函数都会中断执行</font>。

```javascript
function pe(a) {
    if (a) {
        return new Promise((resolve) => {
            setTimeout(resolve, 1000);
        });
    } else {
        throw new Error("错误");
    }
}
async function f() {
    await pe(false);
    await pe(true); // 不会执行
}

f()
    .then(data => console.log(data))
    .catch(err => console.log(err)); // 错误
```

如果需要实现<font color=red>前一个异步操作失败不会中断后面的异步操作的话，可以使用 try...catch 结构当中</font>

```javascript
async function f() {
    try {
        await Promise.reject("错误");
    } catch(e) {}
    return await Promise.resolve("Hello World！");
}
f()
    .then(data => console.log(data)) // Hello World！
    .catch(err => console.log(err));
```

### 4.<span id="mdjump_04-04">错误处理</span>
await 后面的异步操作出错等同于 async 函数返回的 Promise 对象为 reject，错误信息会被 catch 方法接收并返回到方法的回调函数的参数中。

```javascript
async function f() {
    await new Promise(() => {
        throw new Error("错误");
    });
}
f()
    .then(data => console.log(data))
    .catch(err => console.log(err));
// Error：出错了
```

### 5.<span id="mdjump_04-05">注意事项</span>
(1) await 命令后面的 Promise 对象，运行结果可能是 rejected ，所以最好把 await 命令放在 try...catch 代码块中。

```javascript
function promise(a) {
    if (a) {
        return new Promise((res, rej) => {
            setTimeout(() => res("pass"), 2000);
        });
    } else {
        throw new Error("error");
    }
}

async function f() {
    let a, b;
    try {
        a = await promise(true);
        b = await promise(false);
    } catch (err) {
        console.log(err);
    }
    return [a, b];
}

f()
    .then(data => console.log(data))
    .catch(err => console.log(err));
// Error: error
// [ 'pass', undefined ]
```

(2) 多个await命令后面的异步操作，如果不存在继发关系，最好让它们同时触发。

(3) await命令只能用在async函数之中，如果用在普通函数，就会报错。

(4) async 函数可以保留运行堆栈。

---
## <span id="mdjump_05">五：async 函数的实现原理</span>
在前面的“[async 函数概述](#mdjump_02)”就有提及：“[async 是 Generator 的语法糖](#mdjump_injump_1)”。

它的原理，不过就是将 Generator 函数和自动执行器，包装在一个函数里。

```javascript
async functionn fn(arguments) {
    // 内容...
}

// 等同于

funtion fn(arguments) {
    return spawn(function* () {
        // 内容...
    });
}
```

而自动执行器 spawn 函数的实现，基本就是前文自动执行器的翻版。

```javascript
function spawn(genF) {
  return new Promise(function(resolve, reject) {
    const gen = genF();
    function step(nextF) {
      let next;
      try {
        next = nextF();
      } catch(e) {
        return reject(e);
      }
      if(next.done) {
        return resolve(next.value);
      }
      Promise.resolve(next.value).then(function(v) {
        step(function() { return gen.next(v); });
      }, function(e) {
        step(function() { return gen.throw(e); });
      });
    }
    step(function() { return gen.next(undefined); });
  });
}
```