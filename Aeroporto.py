teste = 1
while True:
    a, v = map(int,input().split())
    if a == v == 0:
        break

    aeroporto = [0] * a

    while v:
        v -= 1
        x, y = map(int, input().split())
        aeroporto[x-1] = aeroporto[x-1] + 1
        aeroporto[y-1] = aeroporto[y-1] + 1

    m = max(aeroporto)
    maior = [str(i + 1) for i in range(len(aeroporto)) if aeroporto[i] == m]

    print("Teste %d" % teste)
    teste += 1

    for i in range(len(maior)):
        print(maior[i],end=" ")

    print()
    print()
