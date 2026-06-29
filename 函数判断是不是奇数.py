def isOdd(n):
    return n % 2 != 0
s = input("输入整数以判断是不是奇数：")
try:
    n = int(s)
    print(isOdd(n))
except ValueError:
    print("输入非整数")