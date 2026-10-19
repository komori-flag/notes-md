# @snippet errors
张三 # 错误
20 # 警告


李四 # 错误
25 # 警告


王五 # 错误
30 # 警告
# @end

# @snippet string
"张三" # 正确
'李四' # 正确
"王五" # 正确
'张三' # 正确
# @end

# @snippet single
'张三' # 正确
'李四' # 正确
# @end

# @snippet multilang
'你好，世界！' # 正确
'hello 时间' # 正确
# @end

# @snippet docstring-double
"""这是一个文档字符串，用于描述当前 py 文件的功能。"""
# @end

# @snippet docstring-single
'''这是一个文档字符串，用于描述当前 py 文件的功能。'''
# @end

# @snippet scratch
# “应当对文档字符串使用三个双引号或三个单引号” 文档字符串应该要写在文档的开头部分
# 作用是对当前的 py 文件进行注释，便于阅读和理解
"""这是一个文档字符串，用于描述当前的 py 文件"""
# 保证风格，官方推荐在文档字符串后空一行
# 文档字符串为可选项
# 字面量
"张三" # 错误
# 字面量
'李四' # 错误
# 字面量
"""王五""" # 错误
# 打印信息
print("张三") # 正确
print(20) # 警告
print('李四') # 正确
print(25) # 警告
print("""王五""") # 正确
print(30) # 警告
# @end
