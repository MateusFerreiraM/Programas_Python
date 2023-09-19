l, c = map(int, input("Linhas e Colunas: ").split())
matriz = []
for i in range(l):
    linha = []
    for j in range(c):
        valor = eval(input("Valor: "))
        linha.append(valor)
    matriz.append(linha)

print("Original:")
for i in range(l):
    print(matriz[i])
    
matriz.sort(key=sum)

print("Ordenada:")
for i in range(l):
    print(matriz[i])
