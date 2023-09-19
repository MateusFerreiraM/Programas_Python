def remove_repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    return l

lista1 = [int(x) for x in input("Preencha a lista 1: ").split()]
lista2 = [int(x) for x in input("Preencha a lsita 2: ").split()]
lista3 = []


if len(lista1) < len(lista2):
    x = len(lista2) - len(lista1)
    lista1.extend([0] * x)
    for i in range(len(lista1)):
        lista3.append(lista1[i])
        lista3.append(lista2[i])
        
elif len(lista1) > len(lista2):
    x = len(lista1) - len(lista2)
    lista2.extend([0] * x)
    for i in range(len(lista2)):
        lista3.append(lista2[i])
        lista3.append(lista1[i])

else:
    x = len(lista2) - len(lista1)
    for i in range(len(lista1)):
        lista3.append(lista1[i])
        lista3.append(lista2[i])

lista3 = remove_repetidos(lista3)
if len(lista1) != len(lista2):
    lista3.remove(0)
print(lista3)