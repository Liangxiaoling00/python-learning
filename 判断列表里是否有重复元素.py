def f(list0):
    set1=set(list0)
    if len(set1)==len(list0):
        return False
    else:
        return True
list1=[1,2,3,4,5]
list2=[1,2,3,4,5,5]
list3=[]
print(f'列表{list1}是否有重复元素：{f(list1)}')
print(f'列表{list2}是否有重复元素：{f(list2)}')
print(f'列表{list3}是否有重复元素：{f(list3)}')