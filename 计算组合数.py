def jiecheng(N):
    if N == 0:
        return 1
    else:
        return N * jiecheng(N-1)

def zuheshu(m, n):
    if n > m:
        print("n不能大于m")
    else:
        result = jiecheng(m) // (jiecheng(n) * jiecheng(m-n))
        print(result)

def main():
    m = int(input("请输入m="))
    n = int(input("请输入n="))
    zuheshu(m, n)

main()
