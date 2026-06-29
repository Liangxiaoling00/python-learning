n = int(input("请输入一个整数："))
if n < 2:
    print("不是素数")
else:
    is_prime = True                 # 先假设是素数
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:              # 找到一个因子
            is_prime = False        # 推翻假设
            break
    if is_prime:                    # 循环结束后判断
        print("是素数")
    else:
        print("no")