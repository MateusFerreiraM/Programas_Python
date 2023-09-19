import random
l, c = map(int, input("Linha e Coluna: ").split())
matriz = []

if l == c:
    for i in range(l):
        linha = []
        for j in range(c):
            linha.append(l)
        matriz.append(linha)

elif l < c:
    for i in range(l):
        linha = []
        for j in range(c):
            valor = random.uniform(5,9.9)
            valor = round(valor, 1)
            linha.append(valor)
        matriz.append(linha)

else:
    for i in range(l):
        linha = []
        for j in range(c):
            valor = random.uniform(-10,-5)
            valor = round(valor, 1)
            linha.append(valor)
        matriz.append(linha)

for i in range(l):
    print(matriz[i])
