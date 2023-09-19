vet = []
aux = -1

for i in range(5):
    vet.append(float(input('Digite um valor: ')))

x = int(input("Digite um valor para ser achado: "))

for i in range(len(vet)):
    if vet[i] == x:
        aux = i

if aux>0:
    print("\nO numero está na",aux+1,"ª posição\n")

else:
    print("\n-1\n")