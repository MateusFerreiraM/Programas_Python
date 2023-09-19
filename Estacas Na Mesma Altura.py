n, h = map(int,input().split())
alturas = []
aux = 0
j = 0
alturas = list(map(int, input().split()))


for i in range(1,len(alturas)):
    x = h - alturas[i-1]
    j += abs(x)
    alturas[i-1] = alturas[i-1] + x
    alturas[i] = alturas[i] + x
    

print(j)

