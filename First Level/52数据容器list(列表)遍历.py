"""
既然数据容器可以存储多个元素,那么,就会有需求从容器内依次取出元素进行操作。
将容器内的元素依次取出进行处理的行为,称之为:遍历、迭代。
1. 掌握使用while循环,遍历列表的元素
2. 掌握使用for循环,遍历列表的元素

"""
def list_while_func():
    """
    使用while循环遍历列表的延时函数
    :return:None
    """
    my_list = ["传智教育","黑马程序员","Python"]
    # 循环控制变量通过下标索引来控制,默认0
    # 每一次循环将下标索引变量+1
    # 循环条件:下标索引变量<列表的元素数量

    # 定义一个变量用来标记列表的下标
    index = 0 # 初始值为0
    while index < len(my_list):
        # 通过index变狼取出对应下标的元素
        element = my_list[index]
        print(f"列表的元素{index}为:{element}")
        # 至关重要，将循环变量(index)每一次循环都+1
        index += 1

list_while_func()

def list_for_func():
    """
    使用for循环遍历列表的延时函数
    :return:None
    """
   # element = my_list[index] ？？？

    index = 0
    my_list = [1,2,3,4,5,6,7]
    # for 临时变量 in 数据容器
    for  element in my_list:
        print(f"列表的元素{index}为{element}")
        index += 1

list_for_func()