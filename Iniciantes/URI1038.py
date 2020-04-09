# Exercício 1038: Lanche.

VALORES = input().split()
COD, QUANT = VALORES

COD = int(COD)
QUANT = int(QUANT)

if COD == 1:
  TOTAL = QUANT * 4
  print("Total: R$ {:.2f}".format(TOTAL))
elif COD == 2:
  TOTAL = QUANT * 4.5
  print("Total: R$ {:.2f}".format(TOTAL))
elif COD == 3:
  TOTAL = QUANT * 5
  print("Total: R$ {:.2f}".format(TOTAL))
elif COD == 4:
  TOTAL = QUANT * 2
  print("Total: R$ {:.2f}".format(TOTAL))
elif COD == 5:
  TOTAL = QUANT * 1.5
  print("Total: R$ {:.2f}".format(TOTAL))