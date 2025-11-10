"""
快速体验函数的开发和应用
函数:是组织好的,可重复使用的,用来实现特定功能的代码段。
可供重复利用的代码段，提高程序的复用性，减少重复性代码，提高开发效率
"""
# name = "itheima"
# length = len(name)
# print(length)

# 需求，统计字符串的长度，不使用内置函数len()
str1 = "itheima"
str2 = "itcast"
str3 = "python"

# 定义一个计数的变量
count = 0
for i in str1:
    count += 1
print(f"字符串{str1}的长度是：{count}")

count = 0
for i in str2:
    count += 1
print(f"字符串{str2}的长度是：{count}")

count = 0
for i in str3:
    count += 1
print(f"字符串{str3}的长度是：{count}")

# 可以使用函数，来优化这个过程
def my_len(data):
    count = 0
    for i in data:
        count += 1
    print(f"字符串{data}的长度是{count}")

# 已组织好的可重复使用，针对特定功能
my_len(str1)
my_len(str2)
my_len(str3)