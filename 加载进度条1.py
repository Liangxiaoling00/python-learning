import time
scale = 36
print("执行开始".center(scale//2, "-"))
start = time.perf_counter()#计时用
for i in range(scale+1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i/scale)*100
    print("\r{:^3.0f}%[{}->{}]".format(c,a,b),end='')#end跟\n联动，刷新效果
    time.sleep(0.05)
print("\n"+"执行结束".center(scale//2,'-'))
