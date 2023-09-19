l, c = map(int, input().split())
matriz = []
for i in range(l):
    linha = []
    for j in range(c):
        linha.append(0)
    matriz.append(linha)

for i in range(l):
    print(matriz[i])
