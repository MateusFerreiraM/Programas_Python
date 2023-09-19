l = 3
c = 3
matriz = []
for i in range(l):
    linha = []
    for j in range(c):
        valor = eval(input("Valor: "))
        linha.append(valor)

    matriz.append(linha)

k = int(input("Qual valor você quer multiplicar: "))

print("\nAntes da Multiplicação")
for i in range(l):
    print(matriz[i])

print("\nDepois da Multiplicação")

for i in range(l):
    matriz[i][i] = matriz[i][i] * k

for i in range(l):
    print(matriz[i])

print()
