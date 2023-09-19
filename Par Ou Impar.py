teste = 1
while True:
    n = int(input())

    if n == 0:
        break

    else:
        jogador1 = str(input())
        jogador2 = str(input())
        resultado = []

        while n:
            n -= 1
            a, b = map(int,input().split())

            if (a + b) % 2 == 0:
                resultado.append(jogador1)

            else:
                resultado.append(jogador2)

        print("Teste %d" %teste)
        teste += 1

        for jogador in resultado:
            print(jogador)

        print()