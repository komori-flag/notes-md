# Map 数据结构
## 一：含义
JavaScript 的对象（Object），本质上是键值对的集合（Hash 结构），但是传统上只能用字符串当作键。这给它的使用带来了很大的限制。

对于一部分复杂数据的存储存在着一定的问题。
```javascript
let obj = {};
obj[true] = "value";
obj[12] = "鼠标";
obj[{a: 1}] = "value";
console.log(Object.keys(obj));
// [ '12', 'true', '[object Object]' ]
// 如果对象当中的键不是为字符串类型，则会输出toString之后的结果
```

为了解决这个问题，ES6 提供了 Map 数据结构。
它类似于对象，也是键值对的集合，但是“键”的范围不限于字符串，各种类型的值（包括对象）都可以被当作键。
```javascript
const m = new Map();
```

---
## 二：对象中的方法
### **1.set()方法**
此方法可以向 Map 当中添加新元素。

<font color=skyblue>需传两个参数：一为需要被加入元素的对象；二为需要被加入元素的键值。</font>

```javascript
// 第一种方式
const m = new Map(),
    obj = {name: "猪八戒"};

m.set(obj, 12); // 添加新元素到m中
console.log(m.get(obj)); // 12

// 第二种方式
const m = new Map([['name', 10], ["age", 18]]);
console.log(m); // { 'name' => 10, 'age' => 18 }
console.log(m.get("name")); // 10
```
### **2.get()方法**
此方法可以用来获取一个 Map 对象中指定的元素。

```javascript
const m = new Map(),
    obj = {name: "猪八戒"};

m.set(obj, 12);
console.log(m.get(obj)); // 12
```

### **3.delete()方法**
此方法可以用来删除一个 Map 对象中指定的元素。
```javascript
const m = new Map(),
    obj = {name: "猪八戒"};

m.set(obj, 12);
console.log(m.delete(obj)); // true
```

### **4.has()方法**
此方法可以用于查询 map 中是否存在指定元素，存在则返回 true。
```javascript
const m = new Map(),
    obj = {name: "猪八戒"};

m.set(obj, 12);
console.log(m.has(obj)); // true
```

### **5.clear()方法**
此方法可以用于删除 map 中所有元素。
```javascript
const m = new Map(),
    obj = {name: "猪八戒"};

m.set(obj, 12);
console.log(m.clear(obj)); // true
console.log(m.get(obj)); // undefined
```

## 三：遍历方法
### **1.keys()方法**
此方法可以用于返回<font color=red>键名</font>
```javascript
const map = new Map([['a', 1], ['b',  2]]);
for (let key of map.keys()) {
    console.log(key);
}
// "a"
// "b"
```

### **2.values()方法**
此方法可以用于返回<font color=red>键值</font>
```javascript
const map = new Map([['a', 1], ['b',  2]]);
for (let key of map.values()) {
    console.log(key);
}
// 1
// 2
```

### **3.entries()方法**
此方法可以用于返回<font color=red>键值对</font>
```javascript
const map = new Map([['a', 1], ['b',  2]]);
for (let key of map.entries()) {
    console.log(key);
}
// [ 'a', 1 ]
// [ 'b', 2 ]
```

### **4.forEach()方法**
此方法可以调用回调函数<font color=red>遍历</font>每个成员
```javascript
const map = new Map([['a', 1], ['b',  2]]);
map.forEach((keys, values) => {
    console.log(`${keys}：${values}`);
});
// 1：a
// 2：b
```

## 四：map与其他数据结构的互相转换
### **1.map转换为数组（使用扩展运算符）**
```javascript
const m = new Map()
    .set(true, 6)
    .set({ foo: 3 }, ["ccb"]);

console.log([...m]); 
// map转数组。 [ [ true, 6 ], [ { foo: 3 }, [ 'ccb' ] ] ]
```

### **2.Map与对象的互换**
```javascript
const obj = {},
    map = new Map([['a', 111], ['b', 222]]);

for (let [key, values] of map) {
    obj[key] = values;
}
console.log(obj); // { a: 111, b: 222 }
```
