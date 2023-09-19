n, f = map(int, input().split())
ciclo = list(map(int, input().split()))
PrimeiroDia = 1
UltimoDia = 10**8

while PrimeiroDia < UltimoDia:

    aux = int((PrimeiroDia + UltimoDia) / 2)
    total = 0

    for i in range(len(ciclo)):
        total = total + (aux // ciclo[i])

    if total >= f:
        UltimoDia = aux
    else:
        PrimeiroDia = aux + 1

print(UltimoDia)
