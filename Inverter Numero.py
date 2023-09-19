'''Mateus Ferreira Machado. Turma A1. Questão 1 da Avaliação 1.'''

num = int(input("Digite um número: "))
cont = 0
invertido = 0
aux = num

print("\nNumero Original:",num, end=" - ")

while aux >= 1:
    aux = aux / 10
    cont = cont + 1

while num >= 1:
    invertido = invertido + (num % 10) * (10**(cont-1))
    num = num // 10
    cont = cont - 1

print("Numero Invertido:",invertido,"\n")