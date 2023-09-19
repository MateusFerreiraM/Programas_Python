N = int(input())
trilha = 0
subida = 0

for i in range (N):
    valores = input()
    valores = valores.split()
    M = int(valores[0])
    contador1 = 0
    contador2 = 0
    altura = int(valores[1])
    
    for j in range(1, M+1):
        alturanova = int(valores[j])
        
        if alturanova > altura:
            contador1 = alturanova - altura + contador1
            
        altura = alturanova

    altura = int(valores[M])
    for k in range(M,0,-1):
        alturanova = int(valores[k])

        if alturanova > altura:
            contador2 = alturanova - altura + contador2

        altura = alturanova

    contador1 = min(contador1, contador2)
    
    if i == 0:
        subida = contador1
        trilha = i+1
    else:
        if contador1<subida:
            subida = contador1
            trilha = i+1

print(trilha)