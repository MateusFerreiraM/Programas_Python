def testa_jogada(posicao,tabuleiro):
    if tabuleiro[posicao[0]][posicao[1]] == "N":
        return "Sim"
    return "Não"

l, c = map(int, input("Linha e coluna: ").split())
matriz = []
for i in range(l):
    linha = []
    for j in range(c):
        linha.append("A")
    matriz.append(linha)

for i in range(l):
    print(matriz[i])

print()

navios = list(map(int,input("Coordenadas dos navios: ").split()))

for i in range(0,len(navios)-1,2):
    matriz[navios[i]] [navios[i+1]] = "N"

for i in range(l):
    print(matriz[i])

tiro = list(map(int,input("Tiro: ").split()))
print(testa_jogada(tiro,matriz))