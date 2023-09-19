n = int(input())
dados = {"A":[],"B":[],"C":[],"D":[],"E":[]}
ordem = "ABCDE"
teste = 1
senha = []
while n != 0:

    for i in range(n):
        i_sequencia = input()
        sequencia = i_sequencia.split()
        numeros = [int(x) for x in sequencia[:10]]
        letras = [y for y in sequencia[10:]]
        k = 0

        for j in ordem:
            dados[j] = [numeros[k],numeros[k+1]]
            k += 2

        if i == 0:
            for letra in letras:
                senha.append(dados[letra])

        else:
            l = 0
            
            for letra in letras:
                if len(senha[l]) > 1:
                    senha[l] = list((set(senha[l])).intersection(set(dados[letra])))
                l += 1
                
    print("Teste %d" % teste)
    teste += 1
    print(senha[0][0],senha[1][0],senha[2][0],senha[3][0],senha[4][0],senha[5][0], end=" ")
    print()
    print()
    senha = []
    n = int(input())
