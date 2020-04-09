# Exercício 1064: Positivos e Média.

TOTAL = 0
SOMA = 0

for i in range(1,7):
  VALOR = float(input())
  if VALOR > 0:
    TOTAL += 1
    SOMA += VALOR
    MEDIA = SOMA/TOTAL
print("{} valores positivos" .format(TOTAL))
print("{:.1f}".format(MEDIA))