def zhaitaozi(day,shengyuT):
    if day==1:
        return shengyuT
    else:
        shengyuT=(shengyuT+1)*2
        return zhaitaozi(day-1,shengyuT)
firstdayzhai=zhaitaozi(10,1)
print(firstdayzhai)
#猴子第1天摘下若干个桃子，
# 吃了一半，还不过瘾，又多吃了一个。
# 第2天早上又将剩下的桃子吃掉一半，
# 又多吃了一个。
# 以后每天早上都吃了前一天剩下的一半另加一个。
# 到第10天早上想再吃时，就只剩下一个桃子了。编写程序，求第1天共摘了多少个桃子。（先确定递归基例和递归链条，递归链条一定要能追踪到递归基例上，否则会产生无限递归的情况）