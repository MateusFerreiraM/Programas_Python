t = 0
p, r = map(int, input().split())
while p != 0 and r != 0:
    t += 1
    
    ordem = list(map(int,input().split()))

    for i in range(r):
        linha = list(map(int,input().split()))
        n = linha[0]
        j = linha[1]

        y = []
        for k in range(n):
            if linha[k+2]==j:
                y.append(ordem[k])
        ordem = y
    print("Teste",t)
    print(ordem[0])
    print()

    p, r = map(int, input().split())
