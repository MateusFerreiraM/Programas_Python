matriculas = list(map(int, input().split()))

for i in range (len(matriculas)-1,-1,-1):
    continuar = input("Deseja Continuar? ")
    if continuar == "N":
        matriculas.pop(i)

    guardando = int(input("guardando lugar para quantas pessoas? "))
    for i in range(guardando):
        matriculas.insert(i,input("Insira a matricula: "))

matriculas = matriculas[:300]
print(matriculas)
