import random
j = [str(i) for i in range(10)]   # 或 ['0','1',...,'9']
passwords = []
for _ in range(30):
    pwd = ''.join(random.choices(j, k=6))
    passwords.append(pwd)
with open("pswd.txt", "w", encoding="utf-8") as f:
    for i in range(0, 30, 6):          # 每行取6个
        line = passwords[i:i+6]
        f.write(' '.join(line) + '\n')