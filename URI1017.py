# Exercício 1017: Gasto de Combustível.

TEMPOGASTO = int(input())
VELOCIDADEMEDIA = int(input())

DISTANCIAPERCORRIDA = VELOCIDADEMEDIA*TEMPOGASTO
LITROS = DISTANCIAPERCORRIDA/12

print("{:.3f}" .format(LITROS))