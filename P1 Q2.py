import math
larg, altura, profund, raio = map(int,input().split())
diametro = 2 * raio
d = math.sqrt(larg**2 + profund**2)
D = math.sqrt(d**2 + altura**2)

if larg > diametro or altura > diametro or profund > diametro:
    print("N")

else:
    if diametro < D:
        print("N")
    else:
        print("S")
