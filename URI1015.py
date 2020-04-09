# Exercício 1015: Distância entre dois pontos.

VALORES1 = input().split(" ")
VALORES2 = input().split(" ")

X1, Y1 = VALORES1
X2, Y2 = VALORES2

DISTANCIA = ((float(X2) - float(X1))**2 + (float(Y2)-float(Y1))**2)**0.5

print("{:.4f}" .format(DISTANCIA))