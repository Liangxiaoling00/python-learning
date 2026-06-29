def multi(*args):
    """返回所有参数的乘积"""
    product = 1
    for num in args:
        product *= num
    return product
# 从键盘读取一行数字，用空格分隔
user_input = input("请输入多个数字，用空格分隔：")
numbers = list(map(float, user_input.split()))  # 将输入转为浮点数列表
# 如果需要整数可改用 int
# numbers = list(map(int, user_input.split()))
# 调用 multi 函数，将列表解包为多个参数
result = multi(*numbers)
print("乘积为:", result)