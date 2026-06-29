list1=[90,92,88,95,89]
list2=[91,91,90,92,90]
list3=[85,82,88,80,86]
list4=[91,91,90,92,90]
list5=[93,95,90,92,89]
def delhl(x):
    x.sort()
    del x[0::4]
    return x
def avg(n):
    he=0
    for i in n:
        he+=int(i)
    avg=he/len(n)
    return round(avg,2)

print("甲的成绩去掉最高最低分后是",delhl(list1) ,'，平均分为',avg(list1))
print("yi的成绩去掉最高最低分后是" , delhl(list2) , '，平均分为' , avg(list2))
print("bing的成绩去掉最高最低分后是" ,delhl(list3) , '，平均分为' , avg(list3))
print("ding的成绩去掉最高最低分后是" , delhl(list4) , '，平均分为' , avg(list4))
print("wu的成绩去掉最高最低分后是" , delhl(list5) , '，平均分为',avg(list5))