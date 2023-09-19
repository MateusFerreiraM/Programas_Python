'''Mateus Ferreira Machado. Turma A1. Questão 1 da Avaliação 2.'''
from math import sqrt

Ax, Ay = map(float, input("Digite Ax e Ay: ").split())
Bx, By = map(float, input("Digite Bx e By: ").split())
Cx, Cy = map(float, input("Digite Cx e Cy: ").split())
Dx, Dy = map(float, input("Digite Dx e Dy: ").split())

AB = sqrt(((Bx-Ax)**2 + (By-Ay)**2))
BC = sqrt(((Cx-Bx)**2 + (Cy-By)**2))
CD = sqrt(((Dx-Cx)**2 + (Dy-Cy)**2))
DA = sqrt(((Ax-Dx)**2 + (Ay-Dy)**2))
AC = sqrt(((Cx-Ax)**2 + (Cy-Ay)**2))

P1 = (AB + BC + AC)/2
P2 = (AC + CD + DA)/2

Ar1 = sqrt((P1*(P1-AB)*(P1-BC)*(P1-AC)))
Ar2 = sqrt((P2*(P2-AC)*(P2-CD)*(P2-DA)))

Atotal = Ar1 + Ar2

print(Atotal)