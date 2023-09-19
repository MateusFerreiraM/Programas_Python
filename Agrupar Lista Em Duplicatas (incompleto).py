lista = [int(x) for x in input("Digite os valores de sua lista (separados por espaço): ").split()]
lista2 = []
y = 1

for i in range(len(lista)-1):
    if lista[i] != lista[i+1]:
        y = 1
        lista2.append(lista[i])

    else:
        y += 1

    lista2.append([lista[i]]*y)

print(lista2)
