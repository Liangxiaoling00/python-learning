w=10000
for i in range(1,21):
    import random
    num=random.randint(1,10)

    if num<5:
        print(f"员工{i},绩效分{num},不发工资，下一位。")
        continue

    if w>0:
        w-=1000
        print(f"向员工{i}发放工资1000元，账户余额还剩余{w}元。")
    else:
        print("工资发完了，下个月领取吧。")
        break

