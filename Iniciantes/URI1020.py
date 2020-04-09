# Exercício 1020: Idade em Dias.

IDADE = int(input())

ANOS = IDADE//365
RESTOANO = IDADE%365
MESES = RESTOANO//30
DIAS = RESTOANO%30

print("{0} ano(s)" .format(ANOS))
print("{0} mes(es)" .format(MESES))
print("{0} dia(s)" .format(DIAS))