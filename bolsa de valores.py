def lucromaximo(bolsa,dias,taxa):
    lucroMaximo = 0
    lucroAtual = lucroFinal = bolsa[0]

    for i in range(dias):
        if((lucroAtual > bolsa[i] and (lucroAtual - bolsa[i] >= taxa)) or bolsa[i] < lucroFinal):
            if lucroAtual - lucroFinal - taxa > 0:
                lucroMaximo += lucroAtual - lucroFinal - taxa

            lucroAtual = lucroFinal = bolsa[i]
        
        if(bolsa[i] > lucroAtual):
            lucroAtual = bolsa[i]

    if(lucroAtual - lucroFinal - taxa > 0):
        lucroMaximo += lucroAtual - lucroFinal - taxa

    return lucroMaximo


dias, taxa = map(int,input().split())
bolsa = [int(x) for x in input().split()]
print(lucromaximo(bolsa,dias,taxa))