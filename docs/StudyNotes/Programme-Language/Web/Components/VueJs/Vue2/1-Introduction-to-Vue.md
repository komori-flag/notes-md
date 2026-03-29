# 初次认识Vue

## 通过 script 标签安装 Vue.js
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- 引入Vue.js -->
    <script type="text/javascript" src="../js/vue.js"></script>
    <script type="text/javascript">
        // 关闭 Vue.js 的生产提示
        Vue.config.productionTip = false;
    </script>
    <title>通过script标签安装Vue.js</title>
</head>
<body>
</body>
</html>
```

## Hello World
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="../js/vue.js"></script>
    <title>Document</title>
    <script>
        Vue.config.productionTip = false;
    </script>
</head>
<body>
    <div id="root">
        <h1>Hello World!</h1>

        <!-- 
            插值表达式（interpolation expression）
            例子：{{ message }}
         -->
        <h1>Hello, {{ name }}</h1>
    </div>

    <!-- 这样写无效，会被当做纯文本处理 -->
    <h1>{{ name }}</h1>

    <script type="text/javascript">
        // 创建一个Vue实例
        new Vue(
            // 配置对象
            {
                // 元素选择器（element selector）
                // 用于指定Vue实例的作用范围，值通常为一个CSS选择器字符串
                el: '#root',
                // el: document.querySelector('#root'), // 同时支持这样的写法
                // el: document.getElementById('root'), // 同时支持这样的写法
                
                // data 对象
                // 用于存储Vue实例的状态数据，可以是任何类型的数据，其可以供模板中的插值表达式使用
                // data: 'World!', // 虽说可以传递任何类型的值，但这样写显然没有意义

                // 通常 data 对象是一个对象，内部为可被引用的属性
                data: {
                    // 这里的 name 属性就可以会被模板中的插值表达式读取
                    name: 'World!'
                },
            }
        );
    </script>
</body>
</html>
```

!!! note "总结"
    1. 想让 Vue 运行，需要创建一个 Vue 实例，并传入一个配置对象；
    2. root 容器内代码必须符合 HTML 语法，否则会被当做纯文本处理；
    3. root 容器内的代码被当做<b style="color: red;"> Vue 模板</b>。


## 问题：
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- 开发版本 Vue -->
    <script src="../js/vue.js"></script>
    <!-- 生产版本 Vue -->
    <script src="../js/vue.min.js"></script>
    <title>Document</title>
    <script>
        Vue.config.productionTip = false;
    </script>
</head>

<body>
    <!-- 
        问题：
     -->

    <!-- 问题1：多个容器问题 -->
    <div class="root">
        <h1>1. Hello, {{ name }}</h1>
    </div>
    <div class="root">
        <h1>2. Hello, {{ name }}</h1>
    </div>

    <!-- 问题2：多个实例对应一个容器问题 -->
    <div id="root">
        <h1>1. Hello, {{ name1 }}、{{ name2 }}</h1>
    </div>
    <div id="root1">
        <h1>1. Hello, {{ name1 }}</h1>
    </div>
    <div id="root2">
        <h1>2. Hello, {{ name2 }}</h1>
    </div>

    <!-- 问题3：插值表达式内可以写什么？ -->
    <!-- 
        插值表达式内可以写任何 JavaScript 表达式。
        但注意区分 JS 表达式和 JS 代码（语句）。
    -->
    <div id="root">
        <h1>1. Hello, {{ name1 }}、{{ name2 }}</h1>
        <p>{{ 1 + 1 }}</p>
        <p>{{ Date.now() }}</p>
        <p>{{ ((a) => a + 1)(1) }}</p>
        <p>{{ 1 == 1 ? 'true' : 'false' }}</p>

        <p>
            Error compiling template:

            avoid using JavaScript keyword as property name: "if"
              Raw expression: {{ if(true){} }}
        </p>
        <p>{{ if(true){} }}</p>
    </div>

    <!-- 问题4：为什么需要通过 Vue 实例来管理数据？ -->
    <div class="root">
        <h1>Hello, {{ name1 }} {{ name2 ? `、${name2}` : '' }}</h1>
        <p>{{ name1.toUpperCase() }}</p>
    </div>

    <!-- 问题5：使用开发版本不实例化 Vue 实例直接运行会如何？ -->
    <div id="root">
        <h1>Hello, {{ name1 }} {{ name2 ? `、${name2}` : '' }}</h1>
    </div>

    <script type="text/javascript">
        // 问题1：多个容器问题
        // 创建一个Vue实例
        new Vue(
            // 配置对象
            {
                // 元素选择器（element selector）
                el: '.root',
                // 数据对象（data object）
                data: {
                    name: 'World!'
                },
            }
        );

        // 问题2：多个实例对应一个容器问题
        // 创建一个Vue实例
        new Vue(
            // 配置对象
            {
                // 元素选择器（element selector）
                el: '#root',
                // 数据对象（data object）
                data: {
                    name1: 'xixi!'
                },
            }
        );
        // 创建一个Vue实例
        /**
         * 第一个实例已经监管了'#root'的情况下，
         * 如果第二个实例再次监管同一个容器会无效。
         * 
         * 一个容器只能对应一个 Vue 实例。
         * - 总结：容器与 Vue 对象间只能一对一。
        */
        new Vue(
            // 配置对象
            {
                // 元素选择器（element selector）
                el: '#root',
                // 数据对象（data object）
                data: {
                    name2: 'haha!'
                },
            }
        );
        new Vue({
            el: '#root1',
            data: {
                name1: 'xixi!'
            }
        });
        new Vue({
            el: '#root2',
            data: {
                name2: 'haha!'
            }
        });

        // 问题3：插值表达式内可以写什么？
        new Vue({
            el: '#root',
            data: {
                name1: 'xixi!',
            }
        })

        // 问题4：为什么需要通过 Vue 实例来管理数据？ 
        const vue = new Vue({
            el: '.root',

            /**
             * 因为数据是会动态变化的，
             * 所以需要通过 Vue 实例来管理数据。
             * 
             * 有什么特点呢？
             * - 1. 数据变化时视图会自动更新。
            */
            data: {
                name1: 'xixi!',
                name2: 'haha!'
            }
        })

        // 问题5：使用开发版本不实例化 Vue 实例直接运行会如何？
        // 开发版本：
        /**
         * [Vue warn]: Vue is a constructor and should be called with the `new` keyword
         vue.min.js:11  Uncaught TypeError: Cannot read properties of undefined (reading '_init')
           at Er (vue.min.js:11:40386)
           at 4-问题.html:161:9
         */
        // 生产版本：
        /**
         vue.min.js:11  Uncaught TypeError: Cannot read properties of undefined (reading '_init')
           at Er (vue.min.js:11:40386)
           at 4-问题.html:161:9
         */
        Vue({
            el: '#root',
            data: {
                name1: 'xixi!',
                name2: 'haha!'
            }
        });
    </script>

</body>

</html>
```

!!! note "问题总结"
    1. Vue 实例可以管理数据，但只能对应一个容器。
    2. 插值表达式内可以写任何<b style="color: red;"> JavaScript 表达式 </b>，但注意区分<b style="color: yellow;"> JS 表达式</b>和<b style="color: yellow;"> JS代码（语句）</b>。
    3. 插值表达式可以读取 data 对象中所有的属性。
    4. 一旦 data 发生变化，页面中使用到该数据的地方都会自动更新。