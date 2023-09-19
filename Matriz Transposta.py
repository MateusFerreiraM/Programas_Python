l, c = map(int, input("Linhas e Colunas: ").split())
matP = []
for i in range(l):
    linha = []
    for j in range(c):
        valor = eval(input("Valor: "))
        linha.append(valor)
    matP.append(linha)

Mt = []
for i in range(c):
    linhaT = []
    for j in range(l):
        valor = matP[j][i]
        linhaT.append(valor)
    Mt.append(linhaT)

print("\nMatriz Transposta:")
for i in range(c):
    print(Mt[i])
