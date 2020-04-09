# Exercício 1009: Salário com Bônus.

NOME = input()
SALARIOFIXO = float(input())
VENDATOTAL = float(input())

TOTAL = SALARIOFIXO + (VENDATOTAL * 0.15)

print("TOTAL = R$ {:.2f}" .format(TOTAL))