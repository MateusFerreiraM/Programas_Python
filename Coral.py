def coral(cor,s,l):
    if (s%l) != 0:
        return -1
    
    maior = 0
    s = s // l
    for i in range(l):
        if cor[i] > s:
            maior += cor[i] - s

    return maior + 1

n = int(input())
while n != Exception(EOFError):
    notas = [int(x) for x in input().split()]
    soma = sum(notas)
    print(coral(notas,soma,n))
    n = int(input())
