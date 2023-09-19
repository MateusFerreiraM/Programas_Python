c = []
l = int(input("Quantas pessoas? "))
for i in range(l):
    linha = []
    linha.append(input("Nome " + str(i) + ": "))
    linha.append(eval(input("Idade " + str(i) + ": ")))
    c.append(linha)

menor = c[0] [1]
pos = 0 
for i in range(l):
    if c[i] [1] < menor:
        menor = c[i] [1]
        pos = i

for i in range(l):
    print(c[i])

print("O mais novo é",c[pos] [0],"com",c[pos] [1],"anos.")