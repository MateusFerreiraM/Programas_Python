l, c = map(int, input().split())
matriz = []
for i in range(l):

    linha = []
    for j in range(c):
        valor = eval(input())
        linha.append(valor)

    matriz.append(linha)

pares = 0
for linha in matriz:
    for valor in linha:
        if valor % 2 == 0:
            pares += 1

for linha in matriz:
    print(linha)

print("A matriz possui",pares,"números pares.")
