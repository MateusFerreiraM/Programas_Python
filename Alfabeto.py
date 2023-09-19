alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
alfabetoinv = input()
palavra = input()
alfabetoinv = list(alfabetoinv)
palavra = list(palavra)
x = []
y = []

for i in range(len(palavra)):
    pos = alfabetoinv.index(palavra[i])
    x.append(pos)

for i in range(len(x)):
    y.append(alfabeto[x[i]])

print("".join(y))
