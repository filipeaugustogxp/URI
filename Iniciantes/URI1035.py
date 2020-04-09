# Exercício 1035: Teste de Seleção 1.

VALORES = input().split()
A, B, C, D = VALORES

A = int(A)
B = int(B)
C = int(C)
D = int(D)
SOMACD = C+D
SOMAAB = A+B
PAR = A//2

if B > C and D > A and SOMACD > SOMAAB and C > 0 and D > 0 and PAR > 0:
  print("Valores aceitos")
else:
  print("Valores nao aceitos")