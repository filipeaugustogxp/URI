# Exercício 1019: Conversão de Tempo.

N = int(input())

HORAS = N//3600
RESTOHORAS = N%3600
MINUTOS = RESTOHORAS//60
SEGUNDOS = RESTOHORAS%60

print("{0}:{1}:{2}" .format(HORAS, MINUTOS, SEGUNDOS))