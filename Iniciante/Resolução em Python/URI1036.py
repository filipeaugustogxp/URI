# Exercício 1036: Fórmula de Bhaskara.

VALORES = input().split()
A, B, C = VALORES

A = float(A)
B = float(B)
C = float(C)

DELTA = B**2 -4*(A)*(C)
RAIZDELTA = DELTA**(1/2)

if DELTA < 0 or A == 0:
  print("Impossivel calcular")
elif DELTA > 0:
  R1 = (-B + RAIZDELTA)/(2*A)
  R2 = (-B - RAIZDELTA)/(2*A)
  print("R1 = {:.5f}" .format(R1))
  print("R2 = {:.5f}" .format(R2))