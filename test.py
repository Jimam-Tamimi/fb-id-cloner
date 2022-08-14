from random import randint


n1 = 5
n2 = 40

a = 10
t = 1

tL = []
mL = []
tmpList = []
i = 0
while True:
    tmp = randint(n1, n2)
    if (tmp not in tL):
        tL.append(tmp)
        tmpList.append(tmp)
        if len(tmpList) == a // t:
            mL.append(tmpList)
            tmpList = []
        if(len(mL) == t):
            break

print(mL)