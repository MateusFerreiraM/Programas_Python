def formatNumber(num,digits):
    if digits > len(str(num)):
        dif = digits - len(str(num))
        for i in range(dif):
            num = "0" + str(num)
    return num

n = int(input("Numero: "))
dig = int(input("Quantidade de Digitos: "))
print("Saída =",str(formatNumber(n,dig)))
