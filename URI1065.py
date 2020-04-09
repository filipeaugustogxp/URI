# Exercício 1065: Pares entre cinco números.

TOTAL = 0

for i in range(1,6):
  VALOR = float(input())
  if VALOR%2 == 0:
    TOTAL += 1
print("{} valores pares" .format(TOTAL))