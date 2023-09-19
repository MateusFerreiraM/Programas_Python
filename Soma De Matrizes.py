a = []
for i in range(2):
    linha = []
    for j in range(2):
        valor = eval(input("Valor: "))
        linha.append(valor)
    a.append(linha)

print()

b = []
for i in range(2):
    linha = []
    for j in range(2):
        valor = eval(input("Valor: "))
        linha.append(valor)
    b.append(linha)

print()

c = []
for i in range(2):
    linha = []
    for j in range(2):
        linha.append(0)
    c.append(linha)

for i in range(2):
    print(a[i])
print("  +")
for i in range(2):
    print(b[i])
print("  =")

for linha in range(2):
    for colunas in range(2):
        c[linha][colunas] = a[linha][colunas] + b[linha][colunas]

for i in range(2):
    print(c[i])