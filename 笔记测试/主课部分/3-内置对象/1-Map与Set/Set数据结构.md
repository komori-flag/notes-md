# Set 数据结构
## 一：基本
ES6 提供了新的数据结构 Set。它类似于数组，但是成员的<font color=red>值都是唯一的，没有重复的值</font>。

Set 本身是一个<b style="color: red;">构造函数</b>，用来生成 Set 数据结构。
```javascript
let set = new Set(); // 创建一个空集合
```

Set 函数可以<font color=skyblue>接受一个数组作为参数，用来**初始化**</font>。
```javascript
let set = new Set([1, 2, 3, 3]);
console.log(set); // Set(3) { 1, 2, 3 }
```
---

## 二：实例的属性及方法
### 1.size属性
我们可以使用<font color=red size=3>“size”属性</font>来<font color=skyblue>**获取**当前的 Set 实例的**成员数**</font>。
```javascript
let set = new Set([0, 1, 2, 3]);
console.log(set.size); // 4
```

### 3. add()方法
我们可以使用“<font color=red>add()</font>”方法来<font color=skyblue>向 Set 结构**加入成员**</font>，同时返回 Set 结构本身。
```javascript
let set = new Set();
set.add(1).add(2).add(1);
console.log(set); // Set(2) { 1, 2 }
```

### 4.has()方法
我们可以使用<font color=red size=3>“has()”方法</font>来<font color=skyblue>**确认**传参的参数是否为当前的 Set 实例的成员</font>。

使用此方法会返回一个布尔值，用于表示添加的值是否为 Set 的成员。
```javascript
let set = new Set([0, 1, 2, 3, 4, 5]);
console.log(set.has(0)); // true
console.log(set.has(6)); // false
```

### 5.delete()方法
我们可以使用<font color=red size=3>“delete()”方法</font>来<font color=skyblue><font color=red>删除</font>当前的 Set 实例的某一个成员</font>。

使用此方法会返回一个布尔值，用于表示删除是否成功。
```javascript
let set = new Set([0, 1, 2, 3, 4, 5]);
console.log(set.delete(6)); // false
console.log(set.delete(1)); // true
console.log(set); // Set(5) {0, 2, 3, 4, 5}
```
### 6.clear()方法
使用此方法可以对 Set 实例下的所有成员实行<font color=red size=3>删除</font>操作。
```javascript
let set = new Set([0, 1, 2, 3, 4]);
set.clear();
console.log(set); // Set(0) {}
```

---
## 三：遍历操作
Set 结构的实例有四个遍历方法，可以用于遍历成员。

### **1.keys()、values()、entries()方法**
使用这些方法都可以返回遍历器对象。

由于 Set 结构没有键名，只有键值（或者说键名和键值是同一个值），所以keys方法和values方法的行为完全一致。

Set 结构的实例<font color=skyblue size=3>默认可遍历</font>
```javascript
let set = new Set(["red", "green", "blue"]);

console.log("默认方法遍历");
for (let i of set) {
    console.log(i);
}
// red
// green
// blue

console.log("keys()方法");
for (let i of set.keys()) {
    console.log(i);
}
// red
// green
// blue

console.log("values()方法");
for (let i of set.values()) {
    console.log(i);
}
// red
// green
// blue

console.log("entries()方法");
for (let i of set.entries()) {
    console.log(i);
}
// ["red", "red"]
// ["green", "green"]
// ["blue", "blue"]

// 由于使用entries方法返回的遍历器，同时包括键名和键值，所以每次输出一个数组，它的两个成员完全相等。
```

### **2.forEach()方法**
此方法可以对每个成员执行某种操作，没有返回值。

forEach方法还可以有第二个参数，表示绑定处理函数内部的this对象。
```javascript
let set = new Set([0, 1]);

// forEach方法有3个参数：键值、键名、集合本身。
// Set 结构的键名就是键值（两者是同一个值），因此第一个参数与第二个参数的值永远都是一样的。
set.forEach((value, key) =>  
    console.log(`Key：${key}，Value：${value}`)
);
// Key：0，Value：0
// Key：1，Value：1
```

### **3.遍历的应用**
扩展运算符和 Set 结构相结合，就可以去除数组的重复成员。
```javascript
let arr = [...new Set([0, 1, 2, 3, 3, 4, 4, 5])];
console.log(arr); // [ 0, 1, 2, 3, 4, 5 ]
```
