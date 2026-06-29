#读取文件names.txt中给出的多个人名，请去重后给出独特性人名的统计。输出共有多少个独特人名。
with open("names.txt", "r", encoding="utf-8") as f:
    nametxt=f.read()
    namess=nametxt.split()
    dict1={}
    for name in namess:
        dict1[name]=dict1.get(name,0)+1
    print(len(dict1))
    print(dict1.keys())


#其实用集合更快