# -*- coding: utf-8 -*-

'''
Napisz program, kt�ry b�dzie symulowa� rzuty kostk� dla dw�ch u�ytkownik�w. W ka�dej turze ka�dy zawodnik rzuca dwiema kostkami. Tur� wygrywa ten zawodnik, kt�ry na samym ko�cu (po okre�lonej ilo�ci tur) b�dzie mia� wi�ksz� ilo�� zwyci�tw.

Je�eli b�dzie remis, gra powinna toczy� si� dalej do pierwszego zwyci�stwa.

Gra powinna:
- posiada� funkcj�, kt�ra b�dzie symulowa�a rzut sze�cienn� kostk� do gry.
- mie� okre�lon� liczb� tur
- podawa� w ka�dej turze wynik rzutu ko�ci� (wylosowan� liczb� oczek) oraz og�lny wynik dla ka�dego u�ytkonika (aktualny bilans zwyci�stw i pora�ek)

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


print "Witaj w grze, rzut koscia !, W ka�dej turze ka�dy zawodnik rzuca dwiema kostkami. Tur� wygrywa ten zawodnik, kt�ry na samym ko�cu (po okre�lonej ilo�ci tur) b�dzie mia� wi�ksz� ilo�� zwyci�tw. "
tury = int(raw_input("Ile tur b�dziemy gra�?\n"))

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
    print "---  Gr� wygrawa gracz number 1 - GRATULACJE  ---"
elif player1_total < player2_total:
    print "---  Gre wygrywa gracz number 2 - GRATULACJE  ---"
