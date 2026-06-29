import random
letters=[chr(i) for i in range(ord('a'), ord('z')+1)]
Letters=[chr(i) for i in range(ord('A'), ord('Z')+1)]
digities = [str(i) for i in range(10)] #或直接用 list('0123456789')
LIst=letters+Letters+digities
pswd=''
for i in range(10):
    m = random.choices(LIst, k=8)
    pswd = ''.join(m)
    print(pswd)
