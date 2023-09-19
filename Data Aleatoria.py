import random

DiaI = int(input("Digite um dia: "))
MesI = int(input("Digite um mês: "))
AnoI = int(input("Digite um ano: "))

DiaF = int(input("Digite outro dia: "))
MesF = int(input("Digite outro mês: "))
AnoF = int(input("Digite outro ano: "))

print(random.randint(DiaI,DiaF), end="/")
print(random.randint(MesI,MesF), end="/")
print(random.randint(AnoI,AnoF))