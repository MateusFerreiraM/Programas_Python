'''Mateus Ferreira Machado. Turma A1. Questão 2 da Avaliação 1.'''

x = int(input("Digite um número inteiro: "))
y = int(input("Digite outro número inteiro: "))

print("\n          Antes\nNúmero 1= ",x,"  Número 2= ",y,"\n")

x = x + y
y = x - y
x = x - y

print("          Depois\nNúmero 1= ",x,"  Número 2= ",y,"\n")