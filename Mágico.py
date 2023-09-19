y,z,v,w = map(int,input().split())
aux = y
x = -1

while (aux <= v):
    if aux % y == 0 and aux % z != 0:
        if v % aux == 0 and w % aux != 0:
            x = aux
            break
    aux = aux + y
print(x)