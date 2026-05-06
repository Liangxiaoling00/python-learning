#控制行的循环i<=9
#控制每一行的输出的循环j<=i
i=1
while i<=9:
    #循环内的变量也别跑出去
    j=1
    while j<=i:
        print(f"{i}*{j}={i*j}\t",end="")
        j+=1
    #print空内容就是一个换行
    print()
    i+=1