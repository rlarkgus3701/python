import random

numlist = (1, 5, 7, 13, 50, 120, 300, 320, 400, 700)

for k in range(10):
    rndNum = numlist[random.randint(0, 9)]
    for n in numlist:
        cntSum += 1
        if n == rndNum:
            break
print(cntSum/10000)