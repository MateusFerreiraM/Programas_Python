altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em Kg: "))
 
IMC = peso / altura**2
 
print("Seu IMC é: %.4f" % IMC)
 
if IMC < 18.5:
    print("Abaixo do peso!")
elif IMC >= 18.5 and IMC < 25:
    print("Saudável!")
elif IMC >= 25 and IMC < 30:
    print("Peso em Excesso!")
elif IMC >= 30 and IMC < 35:
    print("Obesidade Grau 1!")
elif IMC >= 35 and IMC < 40:
    print("Obesidade Grau 2 (severa)!")
else:
     print("Obesidade Grau 3 (mórbida)!")