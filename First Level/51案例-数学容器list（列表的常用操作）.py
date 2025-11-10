"""
常用操作
在Python中,如果将函数定义为class(类)的成员,那么函数会称之为：方法

·列表.append(元素) 向列表中追加一个元素
·列表.extend(容器) 将数据容器的内容依次取出,追加到列表尾部
·列表.insert(下标,元素) 在指定下标处,插入指定的元素
·del 列表[下标] 删除列表指定下标元素
·列表.pop(下标) 删除列表指定下标元素
·列表.remove(元素) 从前向后,删除此元素第一个匹配项
·列表.clear() 清空列表
·列表.count(元素) 统计此元素在列表中出现的次数
·列表.index(元素) 查找指定元素在列表的下标,找不到报错ValueError
·len(列表) 统计容器内有多少元素
"""
# 1. 定义这个列表,并用变量接收它
list = [21,25,21,23,22,20]
print(list)

# 2. 追加一个数字31,到列表的尾部
list.append(31)
print(list)

# 3. 新列表[29,33,30],到列表的尾部
list2 = [29,33,30]
list.extend(list2)
print(list)

# 4. 取出第一个元素(应是:21)
element1 = list.pop(0)
print(element1)

# 5. 取出最后一个元素(应是:30)
element2 = list.pop(-1)
print(element2)

# 6. 查找元素31,在列表中的下标位置
index = list.index(31)
print(f"元素31在列表的下标位置是:{index}")
print(f"最后列表的内容是:{list}")
