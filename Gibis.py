n,c,m = map(int,input().split())
capa = list(input().split())
volumes = list(input().split())
cont = 0

for j in range(len(capa)):
    if not(capa[j] in volumes):
        cont += 1

print(cont)