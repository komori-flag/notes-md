# let 与 const 命令
## 一：let 命令
ES6 新增了 let 命令，用来声明变量，它的用法类似于 var 。

### **1.块级作用域内有效**
使用 let 进行声明的变量，`只在 let 命令所在的代码块内（块级作用域内）有效`。

例：
```javascript
// 只在 let 命令所在的代码块内有效
{
    var a = 10;
    let b = 10;
}
console.log(a); // 10
console.log(b); // ReferenceError: a is not defined.

// for循环当中很适合使用 let 声明
for (let i = 0; i < 10; i++) {
    console.log(i); // 1 2 3 ...
}
console.log(i); //  ReferenceError: i is not defined.

// 块级作用域中也很适用
var a = [];
for (let i = 0; i < 10; i++) {
    a[i] = function () {
        // 如 i 使用 var 声明，则会出现数组中9个函数输出全部为9。
        // 原因在于调用输出的var声明的i是同一个变量。
        // 如果使用let声明，声明的变量仅在块级作用域内有效，数组中每一个输出的均会不同。
        console.log(i);
    };
};
a[2](); // 2
```

-----
### **2. 不存在变量提升（声明提前）**
使用 let 进行声明的变量，`不存在变量提升（声明提前）`。
例：
```javascript
console.log(a); // undefined
var a;
console.log(b); // ReferenceError: Cannot access 'b' before initializaton
let b;
```

---
### **3.不可重复声明**
使用 let 进行声明的变量，`不可重复进行声明操作`。

例：
```javascript
var a = 1;
var a = 2;
console.log(a); // 2
let b = 1;
let b = 2;
console.log(b); // SyntaxError: Identifier'b' has already been declared
```
---

# 二：const 命令
ES6 也新增了 const 命令，用来`声明只读的常量`。
一旦声明，常量的值就不能改变。

### **1.不可改变（指地址）**
例：
```javascript
// 声明的只读常量不可修改
const PI = 3.1415926;
console.log(PI); // 3.1415926
PI = 3; // TypeError: Assignment to constant variable.

// 声明的对象内部的属性以及值可以进行修改，但不可修改对象本身
const Obj_01 = {name: "孙悟空"};
Obj_01.name = "猪八戒";
Obj_01.age = 28;
console.log(Obj_01); // {name: "猪八戒", age: 28}
Obj_01 = {name: "孙悟空"}; // TypeError: Assignment to constant variable.
```
### **2.与 let 命令相似**
let 命令所拥有的特点 const 命令也有，const 命令在 let 命令的基础上添加了只读限制。