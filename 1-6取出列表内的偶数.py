alist=[1,2,3,4,5,6,7,8,9,10]
index=0
even_list=[]
while index<len(alist):
    element=alist[index]
    if element%2==0:
        even_list.append(element)
    index=index+1
print(even_list)
