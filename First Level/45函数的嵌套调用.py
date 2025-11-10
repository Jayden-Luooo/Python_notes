"""
所谓函数的嵌套调用指的是一个函数里面又调用了一另外一个函数
"""
# 定义函数func_b
def func_b():
    print("---2---")
# 定义函数func_a,并在内部调用func_b
def func_a():
    print("---1---")

    # 嵌套调用func_b
    func_b()
 
    print("---3---")

# 调用函数func_c
func_a()

# 因为这里先调用的 func_a()，所以先执行a里的