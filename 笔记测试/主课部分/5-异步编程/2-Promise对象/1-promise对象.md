# Promise对象
一： [为什么需要Promise？](#mdjump_01)
二： [Promise概述](#mdjump_02)
三： [Promise用法](#mdjump_03)
> 1. [Promise方法传递给函数的两个参数](#mdjump_03-01)
> 2. [Promise.prototype.then](#mdjump_03-02)
> 3. [Promise.prototype.catch](#mdjump_03-03)
> 4. [Promise.prototype.finally](#mdjump_03-04)
> 5. [Promise.all](#mdjump_03-05)
> 6. [Promise.race](#mdjump_03-06)

---
## 一：<span id="mdjump_01">为什么需要Promise？</span>
在实际的使用中，有非常多的应用场景我们不能立即知道应该如何继续往下执行。最常见的一个场景就是 ajax 请求。

```javascript
let url = '远端服务器地址';
let result;

let XHR = new XMLHttpRequest();
XHR.open('GET', url, true);
XHR.send();

XHR.onreadystatechange = function() {
    if (XHR.readyState == 4 && XHR.status == 200) {
        result = XHR.response;
        console.log(result);
    };
}
```

因为ajax请求需要远端服务端的响应，所以这个时候我们就需要等待，结果出来了之后才知道怎么样继续下去。

在原生 ajax 当中便会利用 onreadystatechange 事件来表示<font color=blue>当该事件触发并且符合一定条件时，才能拿到想要的数据，之后才能开始处理数据</font>。

但如果我们需要按照请求的顺序依次执行ajax的请求的时候，我们就需要在上一个请求完成的地方再写入一个ajax的请求。当出现第三个ajax(甚至更多)仍然依赖上一个请求时，我们的代码就会逐渐变成一场灾难。这场灾难，往往也被称为**回调地狱*（Callback Hell）**。

```javascript
const url_01 = 'https://远端服务器地址1/库1',
      url_02 = 'https://远端服务器地址1/库2',
      XHR_01 = new XMLHttpRequest(),
      XHR_02 = new XMLHttpRequest();

XHR_01.open('GET', url_01, true);
XHR_01.send();
XHR_01.onreadystatechange = function() {
    if (XHR_01.readyState === 4 && XHR_01.status === 200) {
        console.log(XHR_01.response);

        // 伪代码
        XMR_02.open("GET", url_02, true);
        XHR_02.send();
        XHR_02.onreadystatechange = function() {
            if (XHR_02.readyState === 4 && XHR_02.status === 200) {
                console.log(XHR_02.response);
            };
        };
    };
};
```

因此我们需要一个叫做Promise的东西，来解决这个问题。

补充：什么是回调地狱？
> 指的是 js 当中使用大量的异步回调代码导致代码可读性降低的现象。

---
## 二：<span id="mdjump_02">Promise概述</span>
<font color=red> Promise </font>是异步编程当中的一种解决方案，比传统的“回调函数和事件”解决方案更加合理和强大。ES6 原生提供了 Promise 对象。

简单来讲，Promise 就是一个容器对象，在容器对象当中保存着<font color=blue>某个未来将要发生的事件（通常是一个异步操作）</font>，用来传递异步操作的消息。

**Promise 对象有以下两个特点：**
1. **对象的状态不受外界影响**
一个 Promise 对象代表一个异步操作，异步操作存在着三种状态：
> * pending: 初始状态，不是成功或失败状态；
> * fulfilled: 意味着操作成功完成；
> * rejected: 意味着操作失败。

> &nbsp;&nbsp;&nbsp;&nbsp;只有异步操作的结果，可以决定当前是哪一种状态，任何其他操作都无法改变这个状态，这也是 Promise（承诺） 这个名字的由来。
2. **一旦状态改变，就不会再变，任何时候都可以得到这个结果**
Promise对象的状态改变，只有两种可能：
> * pending（进行中） --> fulfilled（已成功）；
> * pending（进行中） --> rejected（已失败）。

只要这两种情况发生，状态就凝固了，不会再变了，会一直保持这个结果，这时就称为 resolved（已定型）。

有了Promise对象，就可以将异步操作以同步操作的流程表达出来，避免了层层嵌套的回调函数。

---
## 三：<span id=mdjump_03>Promise用法</span>
在 ES6 当中，Promise 对象是一个构造函数（Function），可以使用 new 关键字来生成 Promise 对象。

#### 1. <span id="mdjump_03-01">Promise 方法传递给函数的两个参数</span>

Promise 构造函数接受一个函数作为参数，该函数的两个参数分别是 resolve 和 reject ，由 JavaScript 引擎提供。

```javascript
new Promise(function (res, rej) { });
```

分别讲解 resolve 和 reject 两个参数：
> * resolve：可以修改此 Promise 对象的状态为 fulfilled（已成功）；
> * reject：可以修改此 Promise 对象的状态为 rejected（已失败）。
> * 这两个参数都为一个函数，作用在于可以修改 Promise 的状态。

例：
```javascript
let boolean_new = true;
new Promise(function (res, rej) {
    boolean_new ? res("成功！") : rej("失败了");
});
```

#### 2. <span id="mdjump_03-02">Promise.prototype.then</span>

Promise 实例中具有 then 方法，可以接收构造函数中处理的状态变化，并分别对应执行。

then 方法有两个参数：
> 1. 接收resolved（已成功）状态的执行；
> 2. 接收reject（已失败）状态的执行。

```javascript
const promise = new Promise(function (res, rej) {
    true ? res("允许") : rej("不被允许");
});
promise.then(data => console.log(data),
    err => console.log(err));
```

由于 then 方法的执行结果也会返回一个 Promise 对象，因此我们进行链式调用，这也是解决回调地狱的主要方式。

```javascript
new Promise(function (res, rej) {
    true ? res("允许") : rej("不被允许");
})
.then(data => console.log(data))
.then(null, err => console.log(err));
```

#### 3. <span id="mdjump_03-03">Promise.prototype.catch</span>

Promise.prototype.catch() 方法是 .then(null, rejection) 或 .then(undefined, rejection) 的别名，用于指定发生错误时的回调函数。

```javascript
new Promise(function(res, rej) {
    false ? : res("成功") : rej("失败");
})

.then(data => console.log(data))
.catch(err => console.log(err));

// 等同于
.then(data => console.log(data))
.then(null, err => console.log(err));
```

需要注意的是，如果 Promise 状态已经变成 resolved，再抛出错误是无效的。

```javascript
new Promise(function (res, rej) {
    res("OK");
    rej("test");
})
.then(data => console.log(data))
.catch(err => console.log(err));
// "OK"
```

Promise 对象的错误具有“冒泡”性质（例：DOM事件冒泡），会一直向后传递，直到被捕获为止。

#### 4.<span id="mdjump_03-04">Promise.prototype.finally</span>
<font color=red> finally() </font>方法用于<font color=blue>指定不管 Promise 对象<b>最后</b>状态如何，都会执行的操作</font>。（该方法是 ES2018 引入标准的）

finally() 方法不接受任何参数，这意味着没有办法知道，前面的 Promise 状态到底是 fulfilled 还是 rejected 。

```javascript
new Promise(function(res, req) {
    true ? res("成功") : req("失败了");
})
.then(res => console.log(res))
.catch(err => console.log(err))
.finally(() => {
    console.log("Promise 实例运行完毕");
});
// 成功
// Promise 实例运行完毕
```

#### 5.<span id="mdjump_03-05">Promise.all</span>
<font color=red>Promise.all() </font>方法会接收一个 Promise 对象组成的数组作为参数，当这个数组所有的 Promise 对象状态都变成 resolved 或者 rejected 的时候，它才会去调用 then 方法。

**参数可以不是数组，但必须具有 Iterator 接口，且返回的每个成员都是 Promise 实例**。

```javascript
const promise_01 = new Promise(function (res, rej) {
    res("成功");
}),
    promise_02 = new Promise(function (res, rej) {
    res("成功");
});
Promise.all([promise_01, promise_02])
.then(data => console.log(data))
.catch(err => console.log(err))
.finally(() => console.log("已执行完毕"));
// [ '成功', '成功' ]
// 已执行完毕
```

Promise.all 方法的状态由参数中的 Promise 实例的状态决定，两个或多个参数之间的关系类似为“与”运算符。
> * 当多个参数的状态都为 fulfilled 时，方法的状态即为 fulfilled ；
> * 当多个参数当中有一个参数的状态都为 rejected 时，方法的状态即为 rejected 。

```javascript
const pro_1 = new Promise(function (res) {
    res("成功");
}),
    pro_2 = new Promise(function (res, rej) {
        rej("失败了");
    });

Promise.all([pro_1, pro_2])
.then(data => console.log(data))
.catch(err => console.log(err))
.finally(() => console.log("Promise.all 方法已执行完毕"));
// 失败了
// Promise.all 方法已执行完毕
```

注意，如果作为参数的 Promise 实例，自己定义了 catch 方法，那么它一旦被 rejected ，并不会触发 Promise.all() 的 catch 方法。

#### 6.<span id="mdjump_03-06">Promise.race</span>
与 Promise.all 相似的是，Promise.race 都是以一个 Promise 对象组成的数组作为参数，不同的是，只要当数组中的其中一个 Promsie 状态变成 resolved 或者 rejected 时，就可以调用 .then方法了。

简单来说就是，只要有一个 Promise 实例对象<font color=red>首先改变状态时，Promise.race 当中的状态便会变化为首先改变状态的 Promise 实例对象的状态</font>。

```javascript
const pro_1 = new Promise(function (res, rej) {
    setTimeout(() => rej("失败了"), 3000);
    }),
    pro_2 = new Promise(function (res, rej) {
        setTimeout(() => res("成功"), 4000);
    });

Promise.race([pro_1, pro_2])
.then(data => console.log(data))
.catch(err => console.log(err))
.finally(() => console.log("Promise.race 方法已执行完毕"));
// 失败了
// Promise.race 方法已执行完毕
```