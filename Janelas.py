f1,f2,f3 = map(int,input().split())
Ff1 = f1 + 200
Ff2 = f2 + 200
Ff3 = f3 + 200
dif = 0

if f1 > 0:
    dif = f1

if f2 > Ff1:
    dif = dif + (f2 - Ff1)

if f3 > Ff2:
    dif = dif + (f3 - Ff2)

if Ff3 < 600:
    dif = dif + (600 - Ff3)

print(dif*100)
