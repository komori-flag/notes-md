# Symbol类型
## 一：概述
ES5 的对象属性名都是字符串，正因如此便很容易造成属性名有关的冲突。

### 证明
<details>
<summary>关于如何得出 ES5 的对象属性名都是字符串</summary>
{

    我们平时定义的对象，是没有加引号的。
    
    但在json文件当中，对于对象的属性名需要加引号（例：{"name": "孙悟空"}等）。

    怎么证明属性名为字符串呢？
    {
        var stooge = {
            "first_name" : "Jeo",
            "second_name" : "Mike"
        };
        var copy = {
            first_name : "Jeo",
            second_name : "Mike"
        };
        if (stooge.first_name === copy.first_name){
            console.log("1");
        }
        else {
            console.log("2");
        }
        <!-- 输出为“1”，说明对象的属性名为字符串 -->
    }

}
</details>

---

### 概念
ES6 引入了一种新的原始数据类型<font color=red size=3>**Symbol**</font>，表示<font color=red size=3>**独一无二的值**</font>，它是 JavaScript 语言的第七种数据类型。

Symbol 值通过Symbol函数（Symbol()）生成。

也就是说，在 ES6 当中，对象的属性名有两种，一为原本存在的字符串类型；另外一种就是 Symbol 类型。

凡是属性名属于 Symbol 类型，就都是独一无二的，可以保证不会与其他属性名产生冲突。

```javascript
let s = Symbol();
console.log(typeof s); // 输出为“symbol”，说明变量s是 Symbol 数据类型，而不是字符串之类的其他类型。
```

需要注意的是，
* **Symbol函数前<font color=red size=3>不能使用 new 关键字</font>**

这是因为生成的 Symbol <font color=skyblue>是一个原始类型的值，不是对象，所以不能添加属性</font>。基本上，它是一种类似于字符串的数据类型。

```javascript
console.log(Symbol()); // Symbol()
new Symbol(); // TypeError: Symbol is not a constructor（类型错误：Symbol不是一个构造函数）
```


* **Symbol函数<font color=red size=3>可以接受一个字符串作为参数</font>**

<font color=skyblue>表示对 Symbol 实例的描述</font>。主要是为了在控制台显示，或者转为字符串时，比较容易区分。

```javascript
let s_01 = Symbol("name");
console.log(s_01); // Symbol(name)
s_01.toString(); // "Symbol(name)"
/* 
上面代码中，如果不加参数输出都是Symbol()，不利于区分。
有了参数以后，就等于为它们加上了描述，输出的时候就能够分清，到底是哪一个值。
*/
```

* 如果 Symbol 的参数是一个对象，就会调用该对象的toString方法，将其转为字符串，然后生成一个 Symbol 值。

```javascript
const obj = {
  toString() {
    return 'abc';
  }
};
const sym = Symbol(obj);
sym // Symbol(abc)
```

* 相同参数的Symbol函数的<font color=red size=3>**返回值是不相等的**</font>

```javascript
// 以下的str_01与str_02都是Symbol函数的返回值，而且参数相同，但是它们是不相等的。
// 在没有传入字符串作为参数的情况下
let str_01 = Symbol(),
    str_02 = Symbol();
console.log(str_01 === str_02); // false

// 有参数的情况
let str_01 = Symbol('foo');
let str_02 = Symbol('foo');
console.log(str_01 === str_02) // false
```

* Symbol 值<font color=red size=3>**不能与其他类型的值进行运算**</font>，会报错

```javascript
let sym = Symbol("Hello");
console.log(sym + "World！"); // TypeError: can't convert symbol to string

// Symbol 值可以显式转为字符串和布尔值，但不能转换为数值。
let sym = Symbol("Hello");
console.log(String(sym)); // "Symbol(My symbol)"
console.log(Boolean(sym)); // true
console.log(Number(sym)); // TypeError: Cannot convert a Symbol value to a number
```

---
## 二：Symbol 作为属性名
由于每一个 Symbol 值都是不相等的，这意味着<font color=skyblue> Symbol 值可以作为标识符</font>。

用于对象的属性名，就能保证不会出现同名的属性。

这对于一个对象由多个模块构成的情况非常有用，能防止某一个键被不小心改写或覆盖。

```javascript
// 写法
let mySymbol = Symbol();

// 第一种写法
let a = {};
a[mySymbol] = 'Hello!';

// 第二种写法
let a = {
  [mySymbol]: 'Hello!'
};

// 第三种写法
let a = {};
Object.defineProperty(a, mySymbol, { value: 'Hello!' });

// 以上写法都得到同样结果
a[mySymbol] // "Hello!"
```

不过需要<font color=red size=3>注意</font>的是：

* ①： Symbol 值<font color=skyblue>作为对象属性名时</font>，不能用点运算符（对象.属性字符串）。
```javascript
const mySymbol = Symbol(),
    a = {};
a.mySymbol = 'Hello!'; // {mySymbol: 'Hello!'}
console.log(a[mySymbol]) // undefined
console.log(a['mySymbol']) // "Hello!"
// 因为点运算符后面总是字符串，所以不会读取mySymbol作为标识名所指代的那个值，导致a的属性名实际上是一个字符串，而不是一个 Symbol 值。
```

* ②：Symbol <font color=red>值必须放在方括号之中</font>
```javascript
let s = Symbol(),
    obj = {
  [s]: function (arg) { ... }
};

obj[s](123);
// 如果s不放在方括号中，该属性的键名就是字符串s，而不是s所代表的那个 Symbol 值。
```

* ③：Symbol 值作为属性名时，该属性还是公开属性，不是私有属性。
---
## **三：属性名遍历**
### **1.获取Symbol属性的方法**

Symbol 作为属性名，不会出现在“for...in”和“for...of”循环中，也不会被“Object.keys()”、“Object.getOwnPropertyNames()”、“JSON.stringify()”所返回。

但它不是私有属性，通过“<font color=red size=3>Object.getOwnPropertySymbols()</font>”方法，<font color=skyblue>可以获取指定对象的所有 Symbol 属性名</font>。

使用这种方法会返回一个数组，成员是当前对象的所有用作属性名的 Symbol 值。
```javascript
const obj = {};
let a = Symbol("a"),
    b = Symbol("b");

obj[a] = "Hello ";
obj[b] = "World！";

console.log(Object.getOwnPropertySymbols(obj)); // [Symbol(a), Symbol(b)]
```

<font color=skyblue size=3>对比例子：</font>

```javascript
const obj = {};
const foo = Symbol('foo');

obj[foo] = 'bar';

// for...in方法
for (let i in obj) {
  console.log(i); // 无输出
}

// Object.getOwnPropertyNames方法
Object.getOwnPropertyNames(obj) // []

// Object.getOwnPropertySymbols方法
Object.getOwnPropertySymbols(obj) // [Symbol(foo)]
```
---
### **2.返回所有类型的键名的<font color=red size=4> Reflect.ownKeys() </font>方法**
这种方法可以返回所有类型的键名，包括常规键名和 Symbol 键名。
```javascript
let obj = {
    [Symbol("key")]: 1,
    enum: 2,
    age: 13
};

console.log(Reflect.ownKeys(obj)); // ["enum", "nonEnum", Symbol(my_key)]
```

### 3.**非私有的内部方法（为对象定义一些非私有的、但又希望只用于内部的方法）**