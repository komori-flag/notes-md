# @snippet example
# name、age、weight都是标识符
name = 张三'
age = 20
weight = 70
# @end

# @snippet rules
# 能包含：字母、数字、下划线（_）
name2 = "Tom"
age_2 = 20
_weight_ = 70

# 不能以数字开头
3name = "Tom"  # 错误

# 不能包含空格
name 3 = "Tom"  # 错误

# 不能包含特殊字符
_name@name2_ = "Tom"  # 错误
_name-name2_ = "Tom"  # 错误
_name!name2_ = "Tom"  # 错误
_name%name2_ = "Tom"  # 错误

# 区分大小写
Name = "Tom1"
name = "Tom2"
print(Name)  # Tom1
print(name)  # Tom2

# 不能是关键字
as = "Tom"  # 错误
if = "Tom"  # 错误
for = "Tom"  # 错误

# 尽量不要与内置函数同名
print = "Tom"  # 不会发生错误，但覆盖了内置函数
print("Tom")  # 错误：print不是一个可执行的函数


# 简洁清晰，具有描述性
userName = "Tom" # 小驼峰命名法（首字母小写，后续单词首字母大写）
UserName = "Tom" # 大驼峰命名法（所有单词首字母小写）
user_name = "Tom" # 蛇形命名法（所有单词用下划线连接，Python推荐使用）
# @end
