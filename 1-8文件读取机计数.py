f=open('iwanttouseit.txt','r',encoding='UTF-8')
time=0
for line in f.readlines():
    read_line=line.strip()#去除开头和结尾的空格和换行符\n
    tiple_data=read_line.split(' ')
    for word in tiple_data:
        if word==('songha'):
            time+=1
print(time)
f.close()