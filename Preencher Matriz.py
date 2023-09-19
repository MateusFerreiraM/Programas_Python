l, c = map(int, input("Linhas e Colunas: ").split())
matriz = []
for i in range(l):

    linha = []
    for j in range(c):
        #valor = eval(input("pos" + str(i) + "-" + str(j) + "-> "))        
        valor = eval(input("Valor: "))
        linha.append(valor)

    matriz.append(linha)

for i in range(l):
    print(matriz[i])
