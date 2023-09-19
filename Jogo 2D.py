n = int(input())
vet = []
l = []
x = 0
y = 0
k = 0
for i in range(n):
    c = int(input())
    for j in range(c):
        vet.append(str(input()))
        
        if vet[j] == "ESQ":
            x -= 1
        
        elif vet[j] == "DIR":
            x += 1
        
        else:
            y = int(vet[j][5:])
            k = y - 1 
            if vet[k] == "ESQ":
                x -= 1
                vet[j] = vet[k]
            else:
                x += 1
                vet[j] = vet[k]                
    l.append(x)
    x = 0
    for i in range(len(vet)):
        vet.pop()
    
for i in range(len(l)):
    print(l[i])
