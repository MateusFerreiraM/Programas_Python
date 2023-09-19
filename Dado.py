import random

vetor = []
cont = 0

for i in range(50):
    vetor.append(random.randint(1,6))

for i in range(50):
    if(vetor[i] == 6):
        cont = cont + 1

porcentagem = (cont/50)*100
print("A porcentagem de face 6 foi de ",porcentagem,"%.")