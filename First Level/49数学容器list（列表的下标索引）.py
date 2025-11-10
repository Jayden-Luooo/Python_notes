"""
下标索引
使用“下标索引”取出特定位置的数据
"""
# 通过下标索引取出对应位置的数据
name_list = ['Tom','Lily','Rose']
print(name_list[0]) # 结果：Tom
print(name_list[1]) # 结果：Lily
print(name_list[2]) # 结果：Rose

# 反向索引
print(name_list[-1]) # 结果：Rose
print(name_list[-2]) # 结果：Lily
print(name_list[-3]) # 结果：Tom

# 嵌套列表的下标索引
my_list = [[1,2,3],[4,5,6]]
print(my_list[0][0])
print(my_list[0][2])
print(my_list[1][1])
print(my_list[1][2])