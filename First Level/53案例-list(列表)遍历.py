"""
既然数据容器可以存储多个元素,那么,就会有需求从容器内依次取出元素进行操作。
将容器内的元素依次取出进行处理的行为,称之为:遍历、迭代。
1. 掌握使用while循环,遍历列表的元素
2. 掌握使用for循环,遍历列表的元素

"""
my_list = [1,2,3,4,5,6,7,8,9,10]



def list_while_func():
    even_list = [] 
    index = 0
    while index < len(my_list):
        num = my_list[index]
        if num % 2 == 0:
            even_list.append(num)
        index += 1 

    print(even_list)

list_while_func()

def list_for_func():
    even_list = [] 
    for element in my_list:
        if element % 2 == 0:
            even_list.append(element)
    print(even_list)

list_for_func()