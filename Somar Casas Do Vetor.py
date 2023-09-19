a = [int(x) for x in input("Digite os valores de sua lista (separados por espaço): ").split()]
soma = 0 
vet = []
x = len(a)
while x > 1:
    for i in range(len(a)-1):
        soma = a[i] + a[i+1]
        vet.append(soma)
        x = x - 1
    print(a)
    while len(a) > 0 : a.pop()
    for i in range(len(vet)-1):
        soma = vet[i] + vet[i+1]
        a.append(soma)
        x = x - 1
    x = len(vet)
    print(vet)
    while len(vet) > 0 : vet.pop()
    