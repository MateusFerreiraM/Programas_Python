vet = []
vetPos = []
vetSemdup = []
x = True

for i in range(5):
    vet.append(eval(input('Digite um valor: ')))

for i in range(5):
    if type(vet[i]) == int and vet[i] > 0:
        vetPos.append(vet[i])

for i in vetPos:
    for j in vetSemdup:
        if j == i:
            x = False
    if x:
        vetSemdup.append(i)

print(vet)
print(vetPos)
print(vetSemdup)
