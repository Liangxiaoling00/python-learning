fr=open('bill.txt','r',encoding='utf-8')
fw=open('bill fix.txt','w',encoding='utf-8')

for line in fr:
    line=line.strip()#清理换行符跟空格，开头跟结尾
    lastword=line.split(',')[5]
    if lastword=='测试':
        continue#跳过这一行
    fw.write(line)
    fw.write('\n')

fr.close()
fw.close()