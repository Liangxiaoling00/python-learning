import random

random.seed(0)                 # 设置随机种子，可复现过程
target = random.randint(0, 1000)

guess_count = 0
guess = -1                     # 初始猜测值设为-1（确保不在0~1000范围内）

while guess != target:
    guess = int(input("请输入你猜的数字（0~1000）："))
    guess_count += 1
    if guess > target:
        print("猜大了，请重猜")
    elif guess < target:
        print("猜小了，请重猜")
    else:
        print(f"猜对了，共猜了{guess_count}次")
