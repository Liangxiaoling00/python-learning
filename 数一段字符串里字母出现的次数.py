s='Everybody in this country should learn how to program a computer,because it teaches you how to think.'
s=s.lower()
s=s.replace(' ','')
dict1={}
for c in s:
    dict1[c]=dict1.get(c,0)+1

items=list(dict1.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in items:
    print(i[0],i[1])