investimento = int(input("Digite o quanto quer investir: "))
juros = eval(input("Digite a taxa de juros mensal: "))
valor = 0
total = 0
valida = "S"
while valida == "S":
    for i in range (1, 13):
        valor = total + investimento 
        total = valor + juros*(valor/100)
    print("Saldo do investimento após 1 ano:", round(valor))
    valida = str(input("Deseja processar mais 1 ano? (S/N)"))