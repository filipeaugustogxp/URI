# Exercício 1010: Cálculo Simples.

LINHA1 = input().split(" ")
LINHA2 = input().split(" ")

CODIGO1, QUANTIDADE1, VALOR1 = LINHA1
CODIGO2, QUANTIDADE2, VALOR2 = LINHA2

TOTAL = ((int(QUANTIDADE1) * float(VALOR1)) + (int(QUANTIDADE2) * float(VALOR2)))

print("VALOR A PAGAR: R$ {:.2f}" .format(TOTAL))