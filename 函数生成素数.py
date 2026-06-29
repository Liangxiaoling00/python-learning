
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
count = 0
for i in range(2, 1000):
    if isPrime(i):
        print(i, end=' ')
        count += 1
        if count % 20 == 0:
            print()