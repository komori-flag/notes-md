# class类
一：[概念](#mdjump_01)
> 1. [class（类）的由来](#mdjump_01_01)
> 1-1 [为何需要类（class）？](#mdjump_01_01_1)
> 1-2 [类与构造函数](#mdjump_01_01_2)
> 1-3 [类的方法与构造函数的 prototype](#mdjump_01_01_3)
> 1-4 [类的特殊之处](#mdjump_01_01_4)
> 2. [constructor 方法](#mdjump_01_02)
> 3. [类的实例](#mdjump_01_03)
> 4. [存（setter）/ 取（getter）值函数](#mdjump_01_04)
> 5. [表达式](#mdjump_01_05)
> 5-1 [属性表达式](#mdjump_01_05_1)
> 5-2 [Class表达式](#mdjump_01_05_2)
> 6. [注意点](#mdjump_01_06)
> 6-1 [严格模式](#mdjump_01_06_1)
> 6-2 [不存在变量声明提升](#mdjump_01_06_2)
> 6-3 [name属性](#mdjump_01_06_3)
> 6-4 [Generator 方法](#mdjump_01_06_4)
> 6-5 [this 的指向](#mdjump_01_06_5)

二：[静态方法](#mdjump_02)
> 1. [静态方法不会被实例所继承](#mdjump_02_01)
> 2. [静态方法的 this 指向](#mdjump_02_02)
> 3. [静态方法可与非静态方法重名](#mdjump_02_03)
> 4. [父类的静态方法，可以被子类继承](#mdjump_02_04)

三：[静态属性](#mdjump_03)

四：[静态块](#mdjump_04)
> 
> 
> 
> 

---
## 一：<span id="mdjump_01">概念</span>
### 1.<span id="mdjump_01_01">class（类）的由来</span>

#### <span id="mdjump_01_01_1">(1) 为何需要类（class）？</span>

在 JS 当中，生成一个实例对象的话需要先定义一个构造函数（Function），再进行实例化得到一个实例对象。

```javascript
// 定义构造函数
function Person(name, age) {
    this.name = name;
    this.age = age;
}

// 对构造函数添加原型方法
Person.prototype.toString = function () {
    return "(" + this.name + ", " + this.age + ")";
}

// 实例化构造函数
let person = new Person("孙悟空", 18);

console.log(person);
// Person { name: '孙悟空', age: 18 }
```

传统的 JS 只有对象的概念，没有类（class）的概念，因为 JS 是基于原型的面向对象语言，原型对象特点就是将属性全部共享给新对象。
这样的写法（定义构造函数 --> 添加原型方法 --> 实例化）相对于其它传统面向对象语言来讲，很有一种独树一帜的感脚，非常容易让新学此门语言的程序员感到困惑。

ES6 则提供了更接近传统面向对象语言的写法，引入了 <font color=red>类（Class）</font>的概念。通过 class 关键字，可以定义类。

#### <span id="mdjump_01_01_2">(2) 类（class）与 构造函数（function）

基本上，<font color=red>ES6 的 class 可以看作是一个构造函数的<b>语法糖</b></font>。

```javascript
function Point(name, age) {
    this.name = name;
    this.age = age;
}

Point.prototype.toString = function () {
    return "(" + this.name + ", " + this.age + ")";
}

// 它等同于

class Point {
    // 构造方法
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    toString() {
        return "(" + this.name + ", " + this.age + ")";
    }
}

// 它们都可以输出
console.log(new Point("孙悟空", 18).toString());
// (孙悟空, 18)
```

在<font color=blue>使用的时候，是直接对类使用 new 命令，与构造函数的用法</font><font color=red size=4><b>完全一致</b></font>。

#### <span id="mdjump_01_01_3">(3) 类的方法 与 构造函数的 prototype 

构造函数的 prototype 属性，在 ES6 的“类”上面是继续存在的，<font color=red size=3>而类的所有方法都定义在类的 prototype 属性上面</font>。

<font color=red>在类的实例上调用方法，相当于是在调用原型上的方法</font>。

```javascript
class Point {
    LogOut(value) { 
        return `值：${value}`;
    }
}

console.log(new Point().LogOut(12));
console.log(Point.prototype.LogOut(12));
// 都是“值：12”
```

<font color=blue>也正由于类是构造函数的语法糖</font>，所以在<font color=red>类当中的 prototype 对象的 constructor() 属性会指向类自身</font>，这与构造函数中 constructor() 属性会指向函数自身的特性相似。

```javascript
class Point { };
console.log(Point.prototype.constructor === Point);// true

// 等同于

function Person() { };
console.log(Person.prototype.constructor === Person);// true
```

#### <span id="mdjump_01_01_4">(4) 类的特殊</span>

<font color=red>类的内部所有定义的方法，都是<b>不可枚举</b>（non-enumerable）的</font>，这一点与 ES5 当中的行为不一样。

类写法：
```javascript
class Point { 
    constructorPoint() { }
    toString() { }
};

console.log(Object.keys(Point.prototype)); 
// []

console.log(Object.getOwnPropertyNames(Point.prototype)); 
// [ 'constructor', 'toString' ]
```

ES5 当中的写法：
```javascript
var Point = function () {};

Point.prototype.toString = function () {};

console.log(Object.keys(Point.prototype));
// [ 'toString' ]

console.log(Object.getOwnPropertyNames(Point.prototype));
// [ 'constructor', 'toString' ]
```

---
### 2.<span id="mdjump_01_02">constructor 方法</span>
<font color=red> constructor() 方法是类的默认方法</font>，通过 new 命令生成对象实例时，会自动添加并调用该方法。

```javascript
function Person(name) {
    this.name = name;
}

// 等同于

class Point {
    constructor(name) {
        this.name = name;
    }
}
```

即使没有定义，在通过 new 命令生成对象实例时，<font color=red>JS 引擎会自动为它添加一个空的 constructor() 方法</font>。

方法会<font color=red>默认返回实例对象（即this）</font>，实例对象完全可以指定返回另外一个对象。

```javascript
class Foo {
  constructor() {
    // Object.create方法可用来创建一个新对象，
    // 使用现有的对象来提供新创建的对象的__proto__。
    return Object.create(null);
  }
}

new Foo() instanceof Foo
// false
```

<font color=red> constructor 外声明的属性都是定义在原型上的，可以称为<b>原型属性（即定义在 class 上）</b></font>。

```javascript
class Point {
    constructor() { }
    toString() { }
}

console.log(Object.getOwnPropertyNames(Point.prototype));
// [ 'constructor', 'toString' ]
```

<font color=red>类必须使用 new 调用，否则会报错</font>。
这是它跟普通构造函数的一个主要区别，普通的构造函数即使不用 new 也可以执行。

```javascript
function Person() {
    console.log(1);
}
Person();
// 1

class Foo { 
    constructor() { 
        console.log(1);
    }
}
Foo();
// TypeError: Class constructor Foo cannot be invoked without 'new'
//（类型错误：类构造函数Foo不能在没有'new'的情况下被调用）
```

---
### 3.<span id="mdjump_01_03">类的实例</span>
<font color=blue>生成类的实例的写法，与 ES5 完全一样，也是使用 new 命令</font>。
如果忘记加上 new 关键字，像函数那样调用 Class ，将会报错。

```javascript
class Point {}

let newpoint = Point();
// TypeError: Class constructor Point cannot be invoked without 'new'
```

与 ES5 中的构造函数一样，<font color=red>实例的属性<b>除非是显式定义在其本身（即定义在 this 对象上），否则都是定义在原型上（即定义在 class 上）</b></font>。

```javascript
class Point { 
    constructor() { 
        this.x = "1";
        this.y = "2";
    }
    toString() { 
        return `(${this.x}, ${this.y})`;
    }
}

let newPointback = new Point();

console.log(newPointback.toString());

// Object.hasOwnProperty会检查对象的自有属性，
// 对象原形上的属性其不会检测。
console.log(Object.hasOwnProperty(newPointback, "toString")); 
// false

// 但是对于原型对象本身来说，
// 这些原型上的属性又是原型对象的自有属性，
// 所以原形对象也可以使用hasOwnProperty()检测自己的自有属性。
console.log(newPointback.__proto__.hasOwnProperty("toString")); 
// true
```

与 ES5 一样，<font color=red>类的所有实例共享一个原型对象</font>。

```javascript
class Point {};
let p1 = new Point(),
    p2 = new Point();

console.log(p1.__proto__ === p2.__proto__);
// true
```

虽然可以通过实例的隐式原型（`__proto__`）属性为“类”当中添加方法，但不推荐这样做，因为这会改变“类”的原始定义，可能会影响到所有的实例。

可以通过使用 Object.getPrototypeOf 方法来获取实例对象的原型，然后再为原型添加方法/属性。

---
### 4.<span id="mdjump_01_04">取（getter）/ 存（setter）值函数</span>
“类”的内部可以使用 **get** 和 **set** 关键字，对某个属性设置存值函数和取值函数，拦截该属性的存取行为。

```javascript
class MyClass {
    // 取
    get prop() {
        return 'getter';
    }
    // 存
    set prop(value) {
        console.log('setter: ' + value);
    }
}

let inst = new MyClass();

console.log(inst.prop = 12);
// setter: 123
// 123

console.log(inst.prop);
// 'getter'
```

---
### 5.<span id="mdjump_01_05">表达式</span>
#### (1) <span id="mdjump_01_05_1">属性</span>
类的属性名，可以采用表达式。

```javascript
let mName = "getArea";

class Point {
    [mName]() {
        // ...
    }
}
```

#### (2) <span id="mdjump_01_05_2">Class</span>
类也可以使用表达式的形式定义。

```javascript
const MyClass = class Me {
    getClassName() {
        return Me.name;
    }
};

console.log(new MyClass().getClassName());

// 在类的外部只能用变量“MyClass”调用
console.log(new Me()); // ReferenceError: Me is not defined
```

如果类的内部没用到的话，可以省略定义类名

```javascript
const MyClass = class {};
```

---
### 6.<span id="mdjump_01_06">注意点</span>
#### <span id="mdjump_01_06_1">(1) 严格模式</span>
<font color=red>类和模块的内部，默认就是严格模式</font>。

为考虑到未来所有的代码，其实都是运行在模块之中，所以 ES6 中把整个语言升级到了严格模式。

#### <span id="mdjump_01_06_2">(2) 不存在变量声明提升</span>
<font color=red>类不存在变量声明提升（hoist）</font>，这一点与 ES5 完全不同。

```javascript
// ES5
new Person();
function Person () {}

// ES6
new Point();// ReferenceError: Cannot access 'Point' before initialization
class Point {};
```

#### <span id="mdjump_01_06_3">(3) name属性</span>
本质上，<font color=blue>ES6 的类只是 ES5 的构造函数的一层包装</font>，<font color=red>因此函数的许多特性都被 Class 继承，包括 name 属性</font>。
而 name 属性总是返回紧跟在 class 关键字后面的类名。

```javascript
class Point { }
console.log(Point.name); // "Point"
```

#### <span id="mdjump_01_06_4">(4) Generator 方法</span>
在某个方法的前面加上星号（*），就表示该方法变成了一个 Generator 函数。

```javascript
class Point {
    * GenFun(get) {
        for (let i of get) {
            yield i;
        }
    }
}

let PromiseArr = [
    new Promise((res) => {
    res("Hello");
    }),
    new Promise((res) => {
    res("World");
    })
],
    GenBack = new Point().GenFun(PromiseArr);

for (let i of GenBack) {
    i.then((a) => console.log(a))
        .catch((err) => console.log(err));
}
// Hello
// World
```

#### <span id="mdjump_01_06_5">(5) this 的指向</span>
类的方法内部如果含有 this ，它默认指向类的实例。

```javascript
class Point {
    This_Confirm(value) { 
        return this === value;
    }
}

// this 由 Point 类指向了变量 PointBack
const PointBack = new Point();

// class类内的 this 不等于实例的 this
console.log(Point.prototype.This_Confirm(PointBack)); // false
// 而实例内的 this 等于其自身
console.log(PointBack.This_Confirm(PointBack)); // true
```

## 二：<span id="mdjump_02">静态方法</span>
### 1.<span id="mdjump_02_01">静态方法不会被实例所继承</span>
类（Class）相当于实例对象中的原型，<font color=blue>所有定义在类当中的方法，都会被实例所继承</font>。

类（Class）的静态属性和静态方法定义在类上，实例不会继承静态属性和静态方法。当需要访问静态属性或调用静态方法时，需要通过类名来进行调用。

如果在一个方法前，加上 `static` 关键字，就表示<font color=red>该方法<b>不会被实例继承</b>，而是<b>需要通过类来调用</b></font>。

而这种方法也被称之为<font color=red size=3><b>静态方法</b></font>。

```javascript
class Foo {
    // 静态方法
    static classMethod() { 
        return "Hello world";
    }
}

// 1.直接在Foo上可以调用此方法
console.log(Foo.classMethod());
// Hello world

// 2.在实例上不存在静态方法
const fooback = new Foo();
console.log(fooback.classMethod());
// TypeError: foo.classMethod is not a function
```

### 2.<span id="mdjump_02_02">静态方法的 this 指向</span>
静态方法如果包含`this`关键字，则<font color=blue> this 的指向为类，不会是实例</font>。

```javascript
class Foo { 
    static This_Confirm(value) { 
        return this === value;
    }
}

// 1.类的this指向为类
console.log(Foo.This_Confirm(Foo)); // true

// 2.类的this不指向为实例
let FooBack = new Foo();
console.log(Foo.This_Confirm(FooBack)); // false
```

### 3.<span id="mdjump_02_03">静态方法可与非静态方法重名</span>

```javascript
class Foo { 
    static classMethod() { 
        return this.TwoLog("Hello");
    }
    static TwoLog(value) { 
        return value;
    }
    classMethod() { 
        return "World";
    }
}

const NewFooBack = new Foo();
console.log(Foo.classMethod()); // Hello
console.log(NewFooBack.classMethod()); // World
```

### 4.<span id="mdjump_02_04">父类的静态方法，可以被子类继承</span>

```javascript
class Foo { 
    static classMethod() { 
        return "Hello World！";
    }
}

class Bar extends Foo { }

console.log(Bar.classMethod());
// Hello World
```

---
## 三：<span id="mdjump_03">静态属性</span>
<font color=red><b>静态属性</b></font>指的是<font color=blue>定义在 类（Class）本身的属性</font>，即 `Class.propName` ，而不是定义在实例对象（this）上的属性。

```javascript
class Foo {

}

Foo.prop = "Hello";
console.log(Foo.prop);
```

但在 ES6 当中，类（Class）的内部只有静态方法，没有静态属性。

在 ES7 当中有一个静态属性的方案， 目前 Babel 转码器支持，这个方案对静态属性规定了一种新的写法。

类的静态属性只要在上面的实例属性写法前面， 加上 `static` 关键字即可。

这种新写法的出现大大方便了对静态属性的表达。

```javascript
class Foo { 
    // 定义一个静态属性
    static myStaticProp = "Hello";
    constructor() {
        console.log(Foo.myStaticProp); // Hello
    }
}

const newFooBack = new Foo();
console.log(newFooBack.myStaticProp); // undefined
```

---
## 四：<span id="mdjump_04">静态块</span>







