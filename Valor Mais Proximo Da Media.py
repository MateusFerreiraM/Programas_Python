vet = list(map(float, input().split()))
menor = 100.0
media = 0
aux = 0

for i in range(len(vet)):
    media = media + vet[i]

media = media / len(vet)

for i in range(len(vet)):
    aux = abs(media - vet[i])

    if aux < abs(menor - media):
        menor = vet[i]

print("A média do vetor é: ",media)
print("O valor mais próximo da média é:",menor)
