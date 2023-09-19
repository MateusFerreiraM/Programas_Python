import sys
import random
 
corredores=[]
melhorVolta=[None, sys.maxsize, -1]
medias=[0]*10
classificacao=[]
 
for i in range(6):
    nome=input('Digite o nome do corredor: ')
    #corredor=[eval(input("Digite o tempo de uma volta: ")) for i in range(10)]
    corredor=[random.randint(0, 1000) for i in range(10)]
 
 
    classificacao.append([sum(corredor), nome])
 
    menorVoltaCorredor=min(corredor) 
    if menorVoltaCorredor<melhorVolta[1]:
        melhorVolta=[nome, menorVoltaCorredor, corredor.index(menorVoltaCorredor)]
 
    for j in range(len(medias)):
        medias[j]+=corredor[j]/10
    corredor.insert(0, nome)
    corredores.append(corredor)

classificacao.sort()
menorMedia=medias.index(min(medias))+1
 
print()
print("A melhor volta foi a de", melhorVolta[0], ', na volta', melhorVolta[2],'.')
print()
print("Classificação: ")
for i in range(6):
    print(str(i+1)+'° -', classificacao[i][1])
 
print()
print("A volta com a média mais rápida foi a", str(menorMedia)+'°.')
print()
print('corredores:',corredores,'médias:', medias,'classificação:', classificacao)