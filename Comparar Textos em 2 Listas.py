def comparaStrings(l1,l2):
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            print("As palavras '",l1[i],"' e '",l2[i],"' são diferentes na posição de índice",i+1,".")

lista1 = list(input().split(" "))
lista2 = list(input().split(" "))
comparaStrings(lista1,lista2)