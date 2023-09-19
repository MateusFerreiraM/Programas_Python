l = 3
c = 3
maior = 0
matriz = []
for i in range(l):
    linha = []
    for j in range(c):
        valor = eval(input("Valor: "))
        linha.append(valor)
    matriz.append(linha)
    
for i in range(3):
    if sum(matriz[i]) > sum(matriz[maior]):
        maior = i

print()

for i in range(3):
    print(matriz[i])

print("\nLinha de maior soma:",maior+1,"\nSoma:",sum(matriz[maior]),"")
