def calcula_media(Valores):
    soma = 0
    for i in range(len(Valores)):
        soma = soma + Valores[i]
        
    media = soma / len(Valores)
    return media
    
def calcula_centroide(pontos):
    x = []
    y = []
    
    for i in range(0,len(coor),2):
        x.append(coor[i])

    for i in range(1,len(coor),2):
        y.append(coor[i])

    mediax = calcula_media(x)
    mediay = calcula_media(y)
    return mediax,mediay

coor = list(map(int,input().split()))
print(calcula_centroide(coor))
