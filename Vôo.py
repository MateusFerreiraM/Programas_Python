def conv(horario):
    hora, minuto = horario.split(':')
    return int(hora)*60 + int(minuto)
    
pA, cB, pB, cA = map(conv,input().split())

duracao = cB + cA - (pA + pB)
duracao = duracao % (60*24)
duracao //= 2

fuso = (cB - (pA + duracao))//60
while fuso < -11:
    fuso += 24
while fuso > 12:
    fuso -= 24
    
print(duracao,fuso)
