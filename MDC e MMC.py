def MDC(a,b):
    mdc = a
    while (a % mdc != 0) or (b % mdc != 0): 
        mdc -= 1
    return mdc
    
def MMC(a,b):
    if a > b:
        maior = a
    else:
        maior = b
    while True:
        if maior % a == 0 and maior % b == 0:
            break
        else:
            maior += 1
    return maior

a,b = map(int,input("Valores: ").split())
print(" MDC=",MDC(a,b),"\n","MMC=",MMC(a,b))