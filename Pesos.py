n = int(input())
caixas = list(map(int, input().split()))
possivel = True
caixas.sort()
for i in range(1,n):
    aux = caixas[i] - caixas[i-1]
    aux = abs(aux)
    if aux > 8 and possivel == True or caixas[0] > 8:
        possivel = False
    
if possivel == True:
    print("S")
else:
    print("N")
