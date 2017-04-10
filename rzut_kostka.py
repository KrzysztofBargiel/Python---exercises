# -*- coding: utf-8 -*-

'''
Napisz program, który bêdzie symulowa³ rzuty kostk¹ dla dwóch u¿ytkowników. W ka¿dej turze ka¿dy zawodnik rzuca dwiema kostkami. Turê wygrywa ten zawodnik, który na samym koñcu (po okreœlonej iloœci tur) bêdzie mia³ wiêksz¹ iloœæ zwyciêœtw.

Je¿eli bêdzie remis, gra powinna toczyæ siê dalej do pierwszego zwyciêstwa.

Gra powinna:
- posiadaæ funkcjê, która bêdzie symulowa³a rzut szeœcienn¹ kostk¹ do gry.
- mieæ okreœlon¹ liczbê tur
- podawaæ w ka¿dej turze wynik rzutu koœci¹ (wylosowan¹ liczbê oczek) oraz ogólny wynik dla ka¿dego u¿ytkonika (aktualny bilans zwyciêstw i pora¿ek)

'''
import random

player1_total = 0
player2_total = 0


def dice_throw():
    sum = 0
    for i in range(0, 2):
        throw = random.randint(1, 6)
        sum += throw
    return sum


print "Witaj w grze, rzut koscia !, W ka¿dej turze ka¿dy zawodnik rzuca dwiema kostkami. Turê wygrywa ten zawodnik, który na samym koñcu (po okreœlonej iloœci tur) bêdzie mia³ wiêksz¹ iloœæ zwyciêœtw. "
tury = int(raw_input("Ile tur bêdziemy graæ?\n"))

while tury > 0:
    player1 = dice_throw()
    player2 = dice_throw()
    dogrywka = False

    print "Gracz 1 rzuca koscia, suma oczek wynosi {}".format(player1)
    print "Gracz 2 rzuca koscia, suma oczek wynosi {}".format(player2)
    if player1 > player2:
        print "Gracz 1 wygral"
        player1_total += 1
    elif player1 < player2:
        print "Gracz 2 wygral"
        player2_total += 1
    elif player1 == player2:
        print "Wyglada na to ze mamy remis - nikt nie dostaje punktu"
    else:
        print "Cos poszlo nie tak - konczymy"
        break

    if tury == 1:
        if player1_total == player2_total:
            print "Wyglada ze mamy remis, DOGRYWKA"
            dogrywka = True
            tury += 1

    print "---  Gracz 1 wygral {} gier, gracz 2 wygral {} gier ---".format(player1_total, player2_total)
    tury -= 1

if player1_total > player2_total:
    print "---  Grê wygrawa gracz number 1 - GRATULACJE  ---"
elif player1_total < player2_total:
    print "---  Gre wygrywa gracz number 2 - GRATULACJE  ---"
