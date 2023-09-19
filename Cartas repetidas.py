n = int(input())
cartas = list(input().split())
cont = 1
maior = 1

for i in range(n-1):
    if cartas[i] == cartas[i+1]:
        cont += 1
    else:
        if cont >= maior:
            maior = cont
            cont = 1
        else:
            cont = 1
print(maior)