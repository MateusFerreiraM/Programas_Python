def countSubStrReverse(text, sub):
    resp = 0
    for i in range(len(text)-1,-1,-1):
        if text[i].upper() == sub.upper():
            resp += 1
    return resp

texto = list(input().split(" "))
palavra = str(input())
print("A string '",palavra,"',aparece",countSubStrReverse(texto,palavra),"vezes no texto.")