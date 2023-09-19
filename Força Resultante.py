vet1 = [] * 3
vet2 = [] * 3
força = [0] * 3

for i in range(3):
    vet1.append(float(input('Digite um valor: ')))
    vet2.append(float(input('Digite outro valor: ')))

for i in range(3):
    força[i] = força[i] + vet1[i] + vet2[i]

print("As forças resultantes são: ",força)