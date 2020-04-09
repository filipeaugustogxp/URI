# Exercício 1060: Números Positivos.

TOTAL = 0

for i in range(1,7):
  VALOR = float(input())
  if VALOR > 0:
    TOTAL += 1
print("{} valores positivos" .format(TOTAL))