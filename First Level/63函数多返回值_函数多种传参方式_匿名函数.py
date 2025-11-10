"""
知道函数如何返回多个值
"""
# 演示使用多个变量，使用多个返回值
def test_return(1,2):
    return 1, "Hello", True # 类型不受限制

x, y, z = test_return()
print(x)
print(y)
print(z)
print(x,y,z)

test_return