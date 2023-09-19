l, c = map(int, input("Linha e Coluna: ").split())
matriz = []
for i in range(l):
    linha = []
    for j in range(c):
        valor = eval(input("Valor: "))
        linha.append(valor)
    matriz.append(linha)

print()

l1, c1 = map(int, input("Linha e Coluna: ").split())
matriz2 = []
for i in range(l1):
    linha = []
    for j in range(c1):
        valor = eval(input("Valor: "))
        linha.append(valor)
    matriz2.append(linha)

print()
for i in range(l):
    print(matriz[i])
print()
for i in range(l1):
    print(matriz2[i])


if c != l1:
    print("\nEssas matrizes não podem ser multiplicadas!")

else:
    mult = []
    for linha in range(l):
        mult.append([])
        for coluna in range(c1):
            mult[linha].append(0)
            for k in range(c):
                mult[linha][coluna] += matriz[linha][k] * matriz2[k][coluna]
    print("\nMultiplicado:")

if l == l1 and c == c1:
    for i in range(c):
        print(mult[i])

else:
    for i in range(c-1):
        print(mult[i])
