media = float(input())

def calcula_status(x):
    if x > 6:
        return "Aprovado"
    elif x < 4:
        return "Reprovado"
    else:
        return "Verificação Suplementar"
print(calcula_status(media))