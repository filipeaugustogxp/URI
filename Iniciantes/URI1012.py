# Exercício 1012: Área.

VALORES = input().split(" ")
A, B, C = VALORES

TRIANGULO = (float(A) * float(C))/2
CIRCULO = 3.14159 * float(C) * float(C)
TRAPEZIO = ((float(A)+float(B)) * float(C))/2
QUADRADO = float(B)**2
RETANGULO = float(A)*float(B)

print("TRIANGULO: {:.3f}" .format(TRIANGULO))
print("CIRCULO: {:.3f}" .format(CIRCULO))
print("TRAPEZIO: {:.3f}" .format(TRAPEZIO))
print("QUADRADO: {:.3f}" .format(QUADRADO))
print("RETANGULO: {:.3f}" .format(RETANGULO))