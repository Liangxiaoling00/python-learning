#先把类型存成变量，方便后面判断
str_type=type("李松河")
int_type=type(510)
float_type=type(6.6)
#待处理的混合数据
data_list=["始皇兔",8.88,66,4.19,"全能ace",78]
#分类容器
str_list=[]
int_list=[]
float_list=[]
#遍历数据，按类型分类
for item in data_list:
    if type(item)==str_type:
        str_list.append(item)
    elif type(item)==int_type:
        int_list.append(item)
    elif type(item)==float_type:
        float_list.append(item)
#输出结果
print("字符串列表：",str_list)
print("整数列表：",int_list)
print("浮点数列表",float_list)