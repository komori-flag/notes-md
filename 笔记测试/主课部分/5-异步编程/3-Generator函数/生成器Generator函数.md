# 生成器 Generator 函数
## 一：概念
Generator 函数是 ES6 提供的一种异步编程解决方案，可以通过 yield 关键字，把函数的执行流挂起，为改变执行流程提供了可能，从而为异步编程提供解决方案、基本用法。

<font color=bluesky>执行 Generator 函数会返回一个遍历器对象，返回的遍历器对象，可以依次遍历 Generator 函数内部的每一个状态</font>。

它有两种区别于普通函数的部分：
> 1. 在普通的“ function ”关键字后会有一个“<font color=red size=3> * </font>”表示为 Generator 函数；
> 2. 函数内部可以使用“<font color=red size=3> yield </font>”表达式用来定义函数内部的状态。

```javascript
// 普通函数
function func_1() {
    return 1;
}
console.log(func_1()); // 输出1，立即执行

// Generator 函数
function* func() {
    yield '1';
    return '2';
}
let newback = func();
console.log(newback.next()); // { value: '1', done: false }
console.log(newback.next()); // { value: '2', done: true }
console.log(newback.next()); // { value: undefined, done: true }
```
上面的代码中可以看到传统函数和 Generator 函数的运行是完全不同的，传统函数调用后立即执行并输出了返回值；而 Generator 函数则没有执行而是返回一个 Iterator 对象，并通过调用 Iterator 对象的 next 方法来遍历。

```javascript
function* func() {
    yield '1';
    yield '2';
    return '3';
}
let newback = func(); // 初始化函数
console.log(newback.next()); // { value: '1', done: false }
console.log(newback.next()); // { value: '2', done: false }
console.log(newback.next()); // { value: '3', done: true }
console.log(newback.next()); // { value: undefined, done: true }
```
上面代码一共调用了三次next方法。

> * 第一次调用时，内部指针从函数头部开始执行，遇到第一个 yield 表达式暂停，并返回当前状态的值；
> * 第二次调用时，内部指针从上一个（即第一个） yield 表达式开始，遇到第二个 yield 表达式暂停，返回当前状态的值；
> * 第三次调用时，内部指针从第二个 yield 表达式开始，当执行遇到 return 语句时便会暂停，并返回当前状态的值。由于执行到这里所有的状态已遍历完毕，因此返回对象中的 done 属性变为 true 表示遍历结束。
> * 第四次调用时，由于函数已经遍历完毕，不再有其它状态，因此返回 `{value: undefined, done: true}`。如果继续调用next方法，返回的也都是这个值。

<font size=3>总结：</font>

> * 当我们使用 Generator 函数时，会返回一个遍历器对象，代表 Generator 函数的内部指针。
> * 每次调用遍历器对象的next方法，就会返回一个有着 value 和 done 两个属性的对象。
> * value属性表示当前的内部状态的值，是yield表达式后面那个表达式的值；done属性是一个布尔值，表示是否遍历结束。

<font size=3>补充：</font>
ES6 没有规定 function 关键字与函数名之间星号的位置，这也就导致无论是什么样的写法都能通过。

```javascript
function * foo(x, y) { ··· }
function *foo(x, y) { ··· }
function* foo(x, y) { ··· }
function*foo(x, y) { ··· }
```

由于 Generator 函数仍然是普通函数，所以一般的写法是上面的第三种，即星号紧跟在function关键字后面。

---
## 二：yield 表达式
由于 Generator 函数返回的是一个遍历器对象，当我们调用 next 方法时才会遍历下一个内部状态，所以提供了一种可以暂停执行的函数。yield表达式就是暂停标志。

（1）yield 表达式只能用在 Generator 函数里面，用在其它地方都会报错
```javascript
function* func1 () {
    yield "输出";
    return "结束输出";
}
console.log(func1().next()); // "输出"

function func2 () {
    yield "输出";
    return "结束输出";
}
console.log(func2().next()); // SyntaxError: Unexpected string
```

（2）yield 表达式如果用在另一个表达式中，必须放在圆括号里
```javascript
function* demo() {
    console.log('Hello' + yield); // SyntaxError
    console.log('Hello' + yield 123); // SyntaxError

    console.log('Hello' + (yield)); // OK
    console.log('Hello' + (yield 123)); // OK
}
```

（3）yield 表达式用作参数或放在赋值表达式的右边，可以不加括号
```javascript
function* demo() {
  foo(yield 'a', yield 'b'); // OK
  let input = yield; // OK
}
```

（4）yield 表达式和 return 语句
> * 相似：<font color=red>都能返回</font>紧跟在语句后面的那个表达式的值；
> * 区别：
> 1. 每次遇到 yield，函数就暂停执行，下一次再从该位置继续向后执行；而 return 语句<font color=red>不具备记忆位置</font>的功能；
> 2. <font color=red>一个函数只能执行一次 return 语句</font>，而在 Generator 函数中可以有任意多个 yield。
```javascript
function* func () {
    yield "1";
    return "2";
    yield "3";
    return "4";
}
let newback = func();
console.log(newback.next()); // { value: "1", done: "false" }
console.log(newback.next()); // { value: "2", done: "true" }
console.log(newback.next()); // { value: "undefined", done: "true" }
```

（5）yield 表达式后的表达式，只有当调用 next 方法、内部指针指向该语句时才会执行；
```javascript
function* gen() {
    yield 123 + 456;
    yield 11 + 22;
}
const newback = gen();
console.log(newback.next()); // { value: 579, done: false }
console.log(newback.next()); // { value: 33, done: false }
console.log(newback.next()); // { value: undefined, done: true }
```

（6）Generator 函数可以不用yield表达式，这时就变成了一个单纯的暂缓执行函数。
> * 函数如果是普通函数，在为变量 generator 赋值时就会执行。
> * 函数是一个 Generator 函数，就变成只有调用 next 方法时，函数才会执行。
```javascript
function* f() {
    console.log('执行了！');
}
let generator = f();

generator(); 
// TypeError: generator is not a function

setTimeout(function () {
    console.log(generator.next());
}, 1000);
// 执行了！
// { value: undefined, done: true }
```

---
## 三：与 Iterator 接口的关系
由于 Generator 函数就是遍历器生成函数，因此可以把 Generator 赋值给对象的Symbol.iterator属性，从而使得该对象具有 Iterator 接口。

```javascript
// 证明 Generator 函数执行后，返回一个遍历器对象中的 Symbol.iterator 属性，执行其属性后是否返回自身。
const mI = function* () {
  yield 1;
},
  newback = mI();
console.log(newback[Symbol.iterator]() === newback);
// true
```

---
## 四：next 方法的参数
yield表达式本身并没有返回值，或者说总是返回 undefined 。

为什么会有返回值？

因为 next 方法可以带一个参数，该参数就会被当作上一个 yield 表达式的返回值。

```javascript
function* f() {
  for(var i = 0; true; i++) {
    var reset = yield i;
    if(reset) { i = -1; }
  }
}

let g = f();

g.next() // { value: 0, done: false }
g.next() // { value: 1, done: false }
g.next(true) // { value: 0, done: false }，next方法带一个参数true时，变量reset就被重置为这个参数
```

Generator 函数从暂停状态到恢复运行，它的<font color=red>上下文状态（context）是不变的</font>。

正因如此，我们可以在 Generator 函数运行的不同阶段，从外部向内部注入不同的值，从而调整函数行为。

例：
```javascript
function* gen(x) {
    let a = 2 * (yield x);
    return a + x;
}
let newback_01 = gen(2),
    newback_02 = gen(2);

newback_01.next(); // { value: 2, done: false }
newback_01.next(); // { value: NaN, done: true }

newback_02.next(); // { value: 2, done: false }
newback_02.next(2); // { value: 6, done: true }
```
> * 上面在 newback_01 中，由于第二次运行 next 方法的时候不带参数，导致 a 的值等于 2 * undefined（即NaN）。
> * 第二次运行 next 方法的时候不带参数，所以 a 等于undefined，返回对象的value属性等于 undefined + NaN，即NaN。
> * 如果向 next 方法提供参数，返回结果便会完全不一样。
> * 由于第二次运行 next 方法的时候带了一个参数，因此在第二次运行时 yield 会返回传入的值，也就是 2 * 2(yield的返回值)，此时 a 为 4 。返回对象的 value 属性等于 4 + 2 ，即6。
> * 需注意的是，由于<font color=bluesky> next 方法的参数表示上一个 yield 表达式的返回值</font>，所以在第一次使用 next 方法时，传递参数是无效的。

---
## 五：for...of 循环
for...of循环可以自动遍历 Generator 函数运行时生成的<font color=red> Iterator </font>对象，且此时不再需要调用next方法。
```javascript
function* foo () {
    yield 1;
    yield 2;
    yield 3;
}

let newarr = [];
for (let i of foo()) {
    newarr.push(i);
}
console.log(newarr); // [ 1, 2, 3 ]
```
> * 上面的代码就使用了 for...of 循环，循环会依次显示 3 个 yield 表达式的值。
> * 一旦 next 方法的返回对象的done属性为 true ，for...of 循环就会中止，<font color=red>且不包含该返回对象</font>。

而除了 for...of 循环以外，扩展运算符（...）、解构赋值和 Array.from 方法内部调用的，都是遍历器接口。它们都可以将 Generator 函数返回的 Iterator 对象，作为参数。

---
## 六：yield* 表达式
有的时候我们需要在 Generator 函数内部，调用另一个 Generator 函数。

ES6 提供了<font color=red> yield* </font>表达式，用来实现<font color=skyblue>在一个 Generator 函数里面执行另一个 Generator 函数</font>。

```javascript
function* newfoo () {
    yield "2 ";
    yield "3 ";
}
function* foo () {
    yield "1 ";
    yield* newfoo();
    yield "4";
}
/*
以上等同于
function* foo () {
    yield "1";
    yield "2";
    yield "3";
    yield "4";
}
*/
let newstr = "";
for (let i of foo()) {
    newstr += i;
}
console.log(newstr); // 1 2 3 4
```

如果在一个 Generator 函数里面执行另一个 Generator 函数时使用 yield 会怎么样？

如果使用 yield ，在执行 Generator 函数下的 next 方法时 value 值将会是一个遍历器对象。

```javascript
function* newfoo () {
    yield "bala";
}
// 使用yield
function* foo_01 () {
    yield newfoo();
}
let newback = foo_01();
newback.next().value; // 返回一个遍历器对象

// 使用yield*
function* foo_02 () {
    yield* newfoo();
}
newback = foo_02();
newback.next().value; // "bala"
```

yield* 后面的 Generator 函数（在没有 return 语句时），等同于在 Generator 函数内部，部署一个 for...of 循环。

且实际上，任何数据结构<font color=bluesky>只要有 Iterator 接口，就可以被 yield* 所遍历</font>。

```javascript
const newarr = [1, 2, 3, 4, 5];
function* concat (i) {
    yield* i;
}

// 相当于
function* concat (i) {
    for (let val of i) {
        yield val;
    }
}

// 获取输出
let newback = concat(newarr);
console.log(newback.next().value); // 1
console.log(newback.next().value); // 2
console.log(newback.next().value); // undefined
```

如果被 Generator 函数所执行的 Generator 函数内部有 return 语句的话，它可以被当做是上一个执行它的 yield* 的返回值。

```javascript
function* newfoo () {
    yield "bala";
    return "fooo";
}
function* foo_01 () {
    let a = yield* newfoo();
    return a;
}
let newback = foo_01();
console.log(newback.next()); // { value: 'bala', done: false }
console.log(newback.next()); // { value: 'fooo', done: true }
console.log(newback.next()); // { value: undefined, done: true }
```

---
## 七：Generator.prototype.return()
Generator 函数返回的遍历器对象，还有一个 return() 方法，可以返回给定的值，并且<font color=red>终结</font>遍历 Generator 函数。

```javascript
function* gen() {
    yield 1;
    yield 2;
}
let b = gen();
console.log(b.next()); // { value: 1, done: false }
console.log(b.return("foo")); // { value: 'foo', done: true }
console.log(b.next()); // { value: undefined, done: true }
```

