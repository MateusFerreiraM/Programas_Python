x1 = float(input("Digite x1: "))
y1 = float(input("Digite y1: "))
x2 = float(input("Digite x2: "))
y2 = float(input("Digite y2: "))
x3 = float(input("Digite x3: "))
y3 = float(input("Digite y3: "))

ab = ((x2-x1)**2 + (y2-y1)**2) ** 1/2
ac = ((x3-x1)**2 + (y3-y1)**2) ** 1/2
bc = ((x3-x2)**2 + (y3-y2)**2) ** 1/2

if ab >= ac+bc or ac >= bc+ab or bc >= ab+ac:
   print(" O Triangulo não existe!")

elif ab == ac and ac == bc:
   print("O Triângulo é equilatero!")

elif ab == ac or ac == bc or bc == ab:
   print("O Triangulo é isosceles!")

else:
   print("O Triangulo é escaleno!")