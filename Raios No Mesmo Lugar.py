n = int(input())
raios = 0
lin = 501
col = 501
coordenadas = [0] * (lin * col)

for i in range(n):
    x, y = map(int, input().split())
    pos = x * col + y
    if coordenadas[pos] == 0:
        coordenadas[pos] = 1
    else:
        raios = 1
        break
print(raios)
