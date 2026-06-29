def fib(n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-1) + fib(n-2)
count=0
list1 = [fib(i) for i in range(1, 21)]
for _ in list1:
    print(f'{_:>5}',end=" ")
    count+=1
    if count%10==0:
        print()#print空本来就是一个换行