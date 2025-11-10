"""
常用操作
在Python中,如果将函数定义为class(类)的成员,那么函数会称之为：方法
"""
mylist = ["itcast","itheima","Python"]

"""
查找某元素的下标:
功能:查找指定元素在列表的下标,如果找不到,报错ValueError
语法:列表.index(列表)
"""
# 1.1 查找某元素在列表内的下标索引              index
xiabiao = mylist.index("itheima")
print(f"itheima的下标索引值是{xiabiao}")

# 1.2 如果被查找的元素不存在，会报错
# xiabiao = mylist.index("hello")
# print(f"hello的下标索引值是{xiabiao}") 

# 2. 修改特定下标索引的值
mylist[0] = "传智教育"
print(f"列表被修改元素后，结果是:{mylist}") 
# 这里将itcast改成了传智教育

# 3. 在指定下标位置插入新元素                   insert
mylist.insert(1,"best wishes")
print(f"列表插入元素后，结果是:{mylist}") 

# 4. 在列表的尾部追加```单个```新元素           append
mylist.append("黑马程序员")
print(f"列表在追加元素后，结果是:{mylist}") 

# 5. 在列表的尾部追加```一批```新元素           extend
mylist2 = [1,2,3]
mylist.extend(mylist2)
print(f"列表在追加一个新的列表后，结果是:{mylist}")

# 6. 删除指定下标索引的元素(2种方式)
# 6.1 方式1:del 列表[下标]                     del
mylist = ["itcast","itheima","Python"]
del mylist[2]
print(f"列表删除元素后的结果是:{mylist}")

# 6.2 方式2:列表.pop(下标)                     pop
mylist = ["itcast","itheima","Python"]
element = mylist.pop(2)
print(f"通过pop方法取出元素后的结果是:{mylist},取出的元素是{element}")

# 7. 删除某元素在列表中的第一个匹配项            remove
mylist = ["itcast","itheima","Python","itcast","itheima"]
mylist.remove("itheima")
print(f"通过remove方法移除元素后，列表的结果是:{mylist}")
# 第一个itheima被删掉了，只能删掉这一个，调用两次可以删掉第二个

# 8. 清空列表                                  clear
mylist = ["itcast","itheima","Python"]
mylist.clear()
print(f"列表被清空了，结果是：{mylist}")

# 9. 统计列表内某元素的数量                     count
mylist = ["itcast","itheima","Python","itcast","itheima"]
num = mylist.count("itheima")
print(f"列表中itheima的数量是:{num}个")

# 10. 统计列表中全部的元素数量                  len
mylist = ["itcast","itheima","Python","itcast","itheima"]
count = len(mylist)
print(f"列表的元素数量为:{count}个")

""" 
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
# 结尾的练习案例