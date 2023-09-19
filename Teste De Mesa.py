n = int(input("Digite um valor: ")

if n < 0:
    print("Erro. Digite um valor positivo.")
    
else:
    r = 1
    while n > 0:
        r = r * n
        n = n - 1
    
    print(r)