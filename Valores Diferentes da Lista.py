lista=[]
contador=0
for i in range(10):
    encontrou=False
    elm=eval(input("Digite um valor: "))

    for j in range(len(lista)):
        if elm==lista[j]:
            encontrou=True

    lista.append(elm)            
    
    if not encontrou:
        contador=contador+1

print(contador)
