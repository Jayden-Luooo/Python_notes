"""
演示数据容器字典的定义
Key: Value对的集合

字典的注意事项：
· 键值对的Key和Value可以是任意类型(Key不可为字典)
· 字典内Key不允许重复,重复添加等同于覆盖原有数据
· 字典不可用下标索引,而是通过Key检索Value
· 字典是无序的,不能通过索引访问
· 字典可以嵌套,即字典内可以包含其他字典
"""

# 定义字典
my_dict = {"张三": 18, "李四": 20, "王五": 19}

# 定义空字典
my_dict_empty = {}

# 定义空字典的另一种方式
my_dict_empty2 = dict()

# 打印字典内容和类型
print(f"my_dict的内容是:{my_dict},类型是:{type(my_dict)}")
print(f"my_dict_empty的内容是:{my_dict_empty},类型是:{type(my_dict_empty)}")
print(f"my_dict_empty2的内容是:{my_dict_empty2},类型是:{type(my_dict_empty2)}")

# 定义重复Key的字典
my_dict_repeat = {"张三": 18, "李四": 20, "王五": 19, "张三": 22}
print(my_dict_repeat)  
# 输出的是后面的张三，前面的被忽略了{'张三': 22, '李四': 20, '王五': 19}

# 字典同集合一样，不可以使用下标索引
my_dict = {"张三": 18, "李四": 20, "王五": 19}
score = my_dict["张三"]  # 使用Key来访问字典中的值
print(f"张三的分数是:{score}")  
score2 = my_dict["李四"]
print(f"李四的分数是:{score2}") 

# 定义嵌套字典
stu_score_dict = {
    "王力宏": {
        "语文": 90, 
        "数学": 95, 
        "英语": 88},
    "周杰伦": {
        "语文": 85, 
        "数学": 92, 
        "英语": 90},
    "林俊杰": {
        "语文": 78, 
        "数学": 80, 
        "英语": 85}
}
print(f"学生的考试信息是:{stu_score_dict}")

# 访问嵌套字典中的值
print(f"王力宏的数学成绩是:{stu_score_dict['王力宏']['数学']}")
print(f"周杰伦的英语成绩是:{stu_score_dict['周杰伦']['英语']}")

"""
演示字典的常用操作
"""
my_dict = {"周杰伦":99, "林俊杰":88, "张学友":77}

# 新增元素
my_dict["张信哲"] = 66
print(f"字典经过新增元素后，结果:{my_dict}")

# 更新元素
my_dict["周杰伦"] = 100  # 更新周杰伦的分数
print(f"字典经过更新元素后，结果:{my_dict}")

# 删除元素
my_dict.pop("林俊杰")  # 删除林俊杰的分数
print(f"字典经过删除元素后，结果:{my_dict}")

# 清空元素
my_dict.clear()  # 清空字典
print(f"字典被清空后变成了：{my_dict}")

# 获取全部的key
my_dict = {"周杰伦":99, "林俊杰":88, "张学友":77}
keys = my_dict.keys()
print(f"字典的全部keys是:{keys}")

# 遍历字典
# 方法1：通过获取到全部的key来完成遍历
for key in keys:
    print(f"字典的key是:{key}")
    print(f"字典的value是:{my_dict[key]}")

# 方法2：直接对字典进行for循环，每一次循环都是直接得到key
for key in my_dict:
    print(f"2字典的key是:{key}")
    print(f"2字典的value是:{my_dict[key]}") 

# 统计字典内的元素数量
num = len(my_dict)
print(f"字典内的元素数量是:{num}")
# 字典支持for循环，但是不支持while循环

"""
演示数据容器的应用场景

· 基于各类数据容器的特点,它们的应用场景如下:

· 列表:一批数据,可修改、可重复的存储场景

· 元组:一批数据,不可修改、可重复的存储场景

· 字符串:一串字符串的存储场景

· 集合:一批数据,去重存储场景

· 字典:一批数据,可用Key检索Value的存储场景
"""

