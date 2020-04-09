# Exercício 1037: Intervalo.

VALOR = float(input())

if 0 <= VALOR <= 25:
  print("Intervalo [0,25]")
elif 25 < VALOR <= 50:
  print("Intervalo (25,50]")
elif 50 < VALOR <= 75:
  print("Intervalo (50,75]")
elif 75 < VALOR <= 100:
  print("Intervalo (75,100]")
else:
  print("Fora de intervalo")