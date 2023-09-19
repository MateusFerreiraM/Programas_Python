def achar(a,b):
    cont = 0
    for i in range(len(a)-2):
        if a[i] == b[0] or a[i+1] == b[0] or a[i+2] == b[0]:
            if a[i] == b[1] or a[i+1] == b[1] or a[i+2] == b[1]:
                cont += 1
            elif a[i] == b[2] or a[i+1] == b[2] or a[i+2] == b[2]:
                cont += 1
            else:
                continue
        
        else:
            if a[i] == b[1] or a[i+1] == b[1] or a[i+2] == b[1]:
                if a[i] == b[2] or a[i+1] == b[2] or a[i+2] == b[2]:
                    cont += 1
                else:
                    break
    return cont

CadeiaA = list(str(input()))
CadeiaB = list(str(input()))

print(achar(CadeiaA,CadeiaB))