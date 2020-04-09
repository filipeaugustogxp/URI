# Exercício 1021: Notas e Moedas.

VALOR = float(input())

NOTAS = [100, 50, 20, 10, 5, 2]
MOEDAS = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")
for NOTA in NOTAS:
  QUANTIDADENOTAS = int(VALOR/NOTA)
  print("{} nota(s) de R$ {:.2f}" .format(QUANTIDADENOTAS,
  NOTA))
  VALOR -= QUANTIDADENOTAS * NOTA

print("MOEDAS:")
for MOEDA in MOEDAS:
  QUANTIDADEMOEDAS = int(round(VALOR, 2)/MOEDA)
  print("{} moeda(s) de R$ {:.2f}".format(QUANTIDADEMOEDAS,
  MOEDA))
  VALOR -= QUANTIDADEMOEDAS * MOEDA