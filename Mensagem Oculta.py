n = int(input())

for i in range(n):
    entrada = input().split()
    saida = ""

    for j in range(len(entrada)):
        saida = saida + entrada[j][0]
    
    print(saida)
    