# while循环

## 循环的作用

循环语句可以让指定的代码块重复执行指定的次数（想重复10次就10次，想重复100次就100次）。

主要有两种循环：
1. **for循环**（后续讲解）：用于遍历序列（如列表、元组、字符串）中的元素。
2. **while循环**（本节重点）：用于在条件为真时重复执行代码块。

## while循环语法

语法结构与if非常相似：

```python
while 条件:
    代码块1
    代码块2
    ...
```

??? note "示例"
    ```python
    i = 1
    while i <= 5:
        print('Hello, World!')
        i += 1
    ```
    输出结果：
    ```
    Hello, World!
    Hello, World!
    Hello, World!
    Hello, World!
    Hello, World!
    ```


1. 循环条件为 True 时继续执行循环；为 False 终止循环。
2. 需要设计好循环条件，避免无限循环。