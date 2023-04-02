# 遍历器（Iterator）
## 一：概述
JavaScript 原有的表示“集合”的数据结构，主要是数组（Array）和对象（Object），在 ES6 当中又添加了 Map 和 Set 数据结构。

用户还可以组合使用这四种不同的数据结构，来定义自己的数据结构。

因此我们需要一种统一的接口机制，来处理所有不同的数据结构。

<font color=red size=3>遍历器（Iterator）</font>就是这样一种机制。它是一种接口，为各种不同的数据结构提供统一的访问机制。任何数据结构只要部署 Iterator 接口，就可以完成遍历操作（即依次处理该数据结构的所有成员）。

它的**作用有三个**：
>1. 为各种数据结构，提供一个统一的、简便的访问接口；
>2. 使得数据结构的成员能够按某种次序排列；
>3.  ES6 创造了一种新的遍历命令 for...of 循环，而Iterator 接口就是主要供 for...of 语句使用。

**遍历器的遍历过程**
>1. 创建一个指针对象，指向当前数据结构的起始位置。也就是说，遍历器对象本质上，就是一个指针对象。
>2. 第一次调用指针对象的next方法，可以将指针指向数据结构的第一个成员。
>3. 第二次调用指针对象的next方法，指针就指向数据结构的第二个成员。
>4. 不断调用指针对象的next方法，直到它指向数据结构的结束位置。
```javascript
// 遍历器
function makeIterator(array) {
    var nextIndex = 0;
    return {
        next: function () {
            return nextIndex < array.length ?
                { value: array[nextIndex++], done: false } :
                { value: undefined, done: true };
        }
    };
}
const items = makeIterator([1, 2]);
console.log(items.next()); 
// 输出为“{ value: 1, done: false }”，指针指向数组中第1个成员
console.log(items.next()); 
// 输出为“{ value: 2, done: false }”，指针指向数组中第2个成员
console.log(items.next()); 
// 输出为“{ value: undefined, done: true }”，数组遍历完成
```

当我们每一次调用next方法时，都会<font color=skyblue>返回数据结构的当前成员的信息（包含value和done两个属性的对象）。</font>
>1. value：当前成员的值；
>2. done：表遍历是否结束，值为布尔值，为 true 表遍历结束。

---
## 二：默认接口
Iterator 接口的目的是<font color=skyblue>为所有数据结构</font><font color=red size=3>提供统一的访问机制（for...of循环）</font>。

**一个数据结构只要具有Symbol.iterator属性，就认为是“可遍历”的。调用Symbol.iterator方法，就会得到当前数据结构默认的遍历器生成函数。**
```javascript
// 以下是一个对象，由于此对象具备Symbol.iterator属性，所以执行这个属性，会返回一个遍历器对象。该对象具有next方法。每次调用next方法，都会返回一个代表当前成员的信息对象，具有value和done两个属性。
const obj = {
  [Symbol.iterator] : function () {
    return {
      next: function () {
        return {
          value: 1,
          done: true
        };
      }
    };
  }
},
newArr = [];
for (let i of obj) {
    newArr.push(i);
}
console.log(newArr); // [1]

// 以下是一个对象，但由于不具有Symbol.iterator属性，因此对象被认为是“不可遍历”的
const obj = {
    name: "集合",
    arr: [
        "集合1",
        "集合2",
        "集合3",
        "集合4"
    ]
}
for (let i of obj) {
    console.log(i);
}
// TypeError: obj is not iterable
```
---
### **关于：数据结构原生具备 Iterator 接口**
<details>
  <summary>点击查看详细内容</summary>

  <p>ES6 的有些数据结构原生具备 Iterator 接口（比如数组），<font color=skyblue>即不用任何处理，就可以被for...of循环遍历</font>。</p>
  
  <p>
    <b>原生具备 Iterator 接口的数据结构如下：</b>
    <ul>
      <li>Array（数组）</li>
      <li>Map</li>
      <li>Set</li>
      <li>String（字符串）</li>
      <li>typedArray</li>
      <li>函数的 arguments 对象</li>
      <li>NodeList 对象</li>
    </ul>
  </p>

  <p>对象（Object）之所以没有默认部署 Iterator 接口，是因为对象的哪个属性先遍历，哪个属性后遍历是不确定的，需要开发者手动指定。</p>
</details>

###
---
一个对象如果要具备可被for...of循环调用的 Iterator 接口，就须在Symbol.iterator的属性上部署遍历器生成方法（原型链上的对象具有该方法也可）。

有了遍历器接口，数据结构就可以用for...of循环遍历，也可以使用while循环遍历。
```javascript
const obj = {
    name: "集合",
    arr: [
        "集合1",
        "集合2",
        "集合3",
        "集合4"
    ],
    [Symbol.iterator]: function () {
        let index = 0;
        return {
            next: () => {
                return index < this.arr.length ?
                    { value: this.arr[index++], done: false } :
                    { value: undefined, done: true };
            }
        }
    }
},
    newArr = [];
for (let i of obj) {
    newArr.push(i);
}
console.log(newArr); // [ '集合1', '集合2', '集合3', '集合4' ]
```

## 三：调用 Iterator 接口的场合
### （1）解构赋值
对数组和 Set 结构进行解构赋值时，会默认调用Symbol.iterator方法。
```javascript
let set = new Set(["a", "b", "c", "d"]),
    [x, y] = set;
// x = 'a', y = 'b'
```

### （2）扩展运算符
扩展运算符（...）也会调用默认的 Iterator 接口。
```javascript
let arr = ["b", "c"],
    newArr = ["a", ...arr, "d"];
// ['a', 'b', 'c', 'd']
```

### （3）yield*
yield*后面跟的是一个可遍历的结构，它会调用该结构的遍历器接口。
```javascript
let generator = function* () {
  yield 1;
  yield* [2];
  yield 3;
},
    iterator = generator();

iterator.next() // { value: 1, done: false }
iterator.next() // { value: 2, done: false }
iterator.next() // { value: 3, done: false }
iterator.next() // { value: undefined, done: true }
```

### （4）其他场合
由于数组的遍历会调用遍历器接口，所以任何接受数组作为参数的场合，其实都调用了遍历器接口。下面是一些例子。
* for...of
* Array.from()
* Map(), Set(), WeakMap(), WeakSet()（比如new Map([['a',1],['b',2]])）
* Promise.all()
* Promise.race()

