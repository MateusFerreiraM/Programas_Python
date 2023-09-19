n = int(input())
c = list(map(int, input().split()))
soma = sum(c)
soma -= (n ** 2 + n) // 2
if soma >= 0 and (soma % n) == 00:
    movimentos = 0
    altura = (soma // n) + 1
    for i in range(n):
        if c[i] > altura:
            movimentos += c[i] - altura
        altura += 1
    print(movimentos)
else:
    print(-1)