# Exercício 1013: O Maior.

VALORES = input().split(" ")
A, B, C = VALORES

A = int(A)
B = int(B)
C = int(C)

MAIORAB = int((A + B + abs(A-B))/2)
TOTAL = int((MAIORAB + C + abs(MAIORAB-C))/2)

print("{} eh o maior" .format(TOTAL))