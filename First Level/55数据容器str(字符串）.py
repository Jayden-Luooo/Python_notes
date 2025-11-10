"""
演示以数据容器的角色,学习字符串的相关操作
str 字符串
字符串是不可修改的 于tuple相似
"""
my_str = "itheima and itcast"
# 通过下标索引取值
value = my_str[2]
value2 = my_str[-16]
print(f"从字符串{my_str}取下标为2的元素，值是：{value}，去下标为-16的元素，值是{value2}")
# my_str[2] = "H" 字符串也不能修改

# index方法
value = my_str.index("and")
print(f"在字符串{my_str}中查找and,其起始下标是：{value}")

# replace方法
"""
字符串的替换
语法:字符串.replace(字符串1,字符串2)
功能:将字符串内的全部:字符串1,替换为字符串2
注意:不是修改字符串本身,而是得到了一个新字符串哦
"""
new_my_str = my_str.replace("it","程序")
print(f"将字符串{my_str}进行替换得到{new_my_str}")

# split方法
"""
字符串的分割
语法:字符串.split(分隔符字符串)
功能:按照指定的分隔符字符串,将字符串划分为多个字符串,并存入列表对象中
注意:字符串本身不变,而是得到了一个列表对象
"""
my_str = "hello python itheima itcast"
my_str_list = my_str.split(" ")
print(f"将字符串{my_str}进行split切分后得到{my_str_list},类型是:{type(my_str_list)}")

# strip字符串的规整操作（去前后空格）
# 语法：字符串.strip()
my_str = " itheima and itcast "
new_my_str = my_str.strip()
print(f"new_my_str的内容是:{new_my_str}")
# 字符串的规整操作（去前后指定字符串）
# 语法：字符串.strip(字符串)
my_str = "1212itheima and itcast1212"
new_my_str = my_str.strip("1212")
print(f"new_my_str的内容是:{new_my_str}")

# 统计字符串中某字符串的出现次数, count
my_str = "itheima and itcast"
count = my_str.count("it")
print(f"字符串{my_str}中it出现的次数是{count}")

# 统计字符串的长度,
length = len(my_str)
print(f"字符串{my_str}的长度是:{length}")

my_str ="黑马程序员"
index = 0
while index < len(my_str):
    print(my_str[index])
    index += 1


my_str ="黑马程序员"
for i in my_str:
    print(i)

"""
给定一个字符串:
'itheima itcast boxuegu'
· 统计字符串内有多少个"it'字符
· 将字符串内的空格,全部替换为字符:
· 并按照”进行字符串分割,得到列表
"""
str = "itheima itcast boxuegu"
num = str.count("it")
print(f"it的总个数为:{num}")
new_str = str.replace(" ","|")
print(f"将空格替换为|后的新字符串为:{new_str}")
final_str = new_str.split("|")
print(f"按照|去分隔后得到了新的字符串:{final_str}")
