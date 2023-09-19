n, m = map(int, input().split())
maior = 0
valor = 0
matriz = []
for i in range(n):
    linha = []
    x = list(map(int,input().split()))
    for i in range(len(x)):
        linha.append(x[i])
    matriz.append(linha)

for i in range(n):
    for j in range(m):
        valor += matriz[i][j]

    if maior < valor:
	    maior = valor

    valor = 0

for i in range(m):
		for j in range(n):
			valor += matriz[j][i]

		if(maior < valor):
			maior = valor

	    valor = 0

print(maior)