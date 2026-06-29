s=input("输入字符串我给你算和：")
def sum_of_digits(s):
    sum=0
    for i in s:
        if i.isdigit():
            sum+=int(i)
    return sum
print(sum_of_digits(s))