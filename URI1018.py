# Exercício 1018: Cédulas.

VALOR = int(input())

if 0 < VALOR < 1000000:
    print(VALOR)

    CED100 = VALOR // 100
    print('%i nota(s) de R$ 100,00' %CED100)

    RESTOCED100 = VALOR % 100
    CED50 = RESTOCED100 // 50
    print('%i nota(s) de R$ 50,00' %CED50)

    RESTOCED50 = RESTOCED100 % 50
    CED20 = RESTOCED50 // 20
    print('%i nota(s) de R$ 20,00' %CED20)

    RESTOCED20 = RESTOCED50 % 20
    CED10 = RESTOCED20 // 10
    print('%i nota(s) de R$ 10,00' %CED10)

    RESTOCED10 = RESTOCED20 % 10
    CED5 = RESTOCED10 // 5
    print('%i nota(s) de R$ 5,00' %CED5)

    RESTOCED5 = RESTOCED10 % 5
    CED2 = RESTOCED5 // 2
    print('%i nota(s) de R$ 2,00' %CED2)

    RESTOCED2 = RESTOCED5 % 2
    CED1 = RESTOCED2 // 1
    print('%i nota(s) de R$ 1,00' %CED1)