resp = 1
while resp == 1:
    n = int(input("Digite um número inteiro: "))
    cont = 0
    for i in range(1, n+1):
        if n%i == 0:
            cont+=1
            print(i,end=" ")
    if cont == 2:
        print("\n",n,"É um numero primo.")
    print("\nDeseja analisar outro número? 1 = Sim | 0 = Não")
    resp = int(input())