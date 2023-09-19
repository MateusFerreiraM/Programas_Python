lista = list(map(int,input().split()))
lista.sort()

if (lista[0] + lista[1] == lista[2] or lista[0] == lista[1] or lista[1] == lista[2]):
	print("S")

else:
    print("N")
    