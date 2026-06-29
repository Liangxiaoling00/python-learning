def dayup(df):
    current=1.0
    for i in range(1,366):
        if i%7 ==6:
            current=current*(1-0.01)
        elif i%7 ==0:
            current=current*(1-0.02)
        else:
            current=current*(1+df)
    return current
dayfactor=0.008
while dayup(dayfactor)<25.0:
    dayfactor +=0.0005
print("每天需要努力：{:.3f}".format(dayfactor))