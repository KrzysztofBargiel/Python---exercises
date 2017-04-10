#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import math

koniec_zadania = "#################################"



'''
Zadanie 1:
Napisz funkcje, która usuwa kazda samogloske z danego stringa
np.   podanie "abcEdfU"  powinno zwrocic "bcdf"
Uwaga na duze i male litery i znaki specjalne
'''


def wyrzuc_wovelsy(s):
    result = re.sub(r'[AEIOU]', '', s, flags=re.IGNORECASE)
    return "Zwrocne slowo to: {}".format(result)

print wyrzuc_wovelsy("abcEdfU")
print koniec_zadania

'''
Zadanie 2
 
Napisz funkcje zliczajaca ilosc wystapien jakiejs liczby na liscie
Na przyklad count([1,2,1,1], 1) powinna zwrocic 3, bo 1 pojawia sie 3 razy na liscie)
Uwaga na puste listy i na liczby, ktorych nie ma liscie
'''


def ilosc_wystapien(x, y):
    return x.count(y)


x = [1, 2, 1, 1]
y = 1
print "W podanej liscie {} cyfra {} wystepuje {} razy".format(x, y, ilosc_wystapien(x,y))
print koniec_zadania

'''
Zadanie 3:
 
Napisz funkcje, ktora zwraca sume wszystkich cyfr z ktorych sklada sie dana liczba
np. digit_sum(1234) powinna zwrocic  10 bo (1 + 2 + 3 + 4)
Uwaga na liczby ujemne i na typy
'''


def digit_sum(num):
    lista = [int(x) for x in str(num)]
    return sum(lista)

print "Suma liczb w liscie jest rowna: {}".format(digit_sum(123))
print koniec_zadania

'''
Zadanie 4:
 
Napisz funkcje, ktora usuwa duplikaty z listy
np. duplikaty([1,1,2,3,4,4]) powinna zwrocic [1,2,3,4]
'''


def duplikaty(lista):
    return list(set(lista))

print "Lista potraktowana funkcja set: {}".format(duplikaty([5, 5, 6, 1, 2, 3, 4, 4]))


def duplikaty(lista):
    nowa_lista = []
    for x in lista:
        if x not in nowa_lista:
            nowa_lista.append(x)
    return nowa_lista

print "Lista dziabnieta na piechote: {}".format(duplikaty([5, 5, 6, 1, 2, 3, 4, 4]))
print koniec_zadania

'''
Zadanie 5:
 
Napisz funkcje factorial, ktora zwraca iloczyn wszystkich cyfr z ktorych sklada sie dana liczba (silnia)
np. factorial(4) powinna zwocic 24  (4 * 3 * 2 * 1 = 24)
factorial z 0 to 1, a z liczb ujemnych nie istnieje (wykorzystaj if, elif i else)
'''


def factorial(liczba):
    return math.factorial(liczba)


print "Silnia policzona funkcja factorial z biblioteki math wynosi: {}".format(factorial(4))
print koniec_zadania


def factorial(liczba):
    silnia = 1
    if liczba == 0:
        return 1
    elif liczba < 0:
        return "Nie policze Ci silni z ujemnej Norbert"
    else:
        for i in range(2, liczba + 1):
            silnia = silnia * i
        return silnia


print "Silnia policzona funkcja na piechote: {}".format(factorial(4))
print koniec_zadania

'''
Zadanie 6:
 
a)
Napisz funkcje, ktora zwraca iloczyn liczb podanych w liscie
np. iloczyn([1,2,3]) powinna zwrocic 6 , poniewaz(1 * 2 *3) = 6
Uwazaj na pusta liste
'''


def iloczyn(lista):
    iloczyn = 1
    if len(lista) == 0:
        return "Lista jest pusta"
    else:
        for x in lista:
            if x >= 0:
                iloczyn *= x
            else:
                return "Liczba ujemna mnie nie interesuje! Koniec"
    return iloczyn


print iloczyn([])
print iloczyn([1, 2, 3, 4])
print iloczyn([1, 2, 3, -4])
print koniec_zadania

'''
Zadanie 7:
 
Napisz funkcje sprawdzajaca, czy dana liczba, jest liczba parzysta
np is_even(3) powinna zwrocic False, a is_even(4) powinna zwrocic True
 
Uwaga: pamietaj o % (modulo, czyli reszta z dzielenia)
'''


def is_even(liczba):
    if liczba % 2 == 0:
        return True
    else:
        return False

a = 4
b = 3
print "Liczba {} jest liczba parzysta? {}".format(a, is_even(a))
print "Liczba {} jest liczba parzysta? {}".format(a, is_even(b))
print koniec_zadania

'''
Zadanie 8:
 
Napisz funkcje, ktora zwracajaca wyraz w odwrotnej kolejnosci
np. odwroc("abc") powinna zwrocic "cba"
 
Mozna to zrobic na kilka sposobow:
- wykorzytujac operator indexowania (string[x:x:x])
- wykorzytujac metode listy
 
Uwaga na typy
'''


def odwroc(arg):
    if type(arg) == str:
        return arg[::-1]
    elif type(arg) == list:
        arg.reverse()
        return arg

a = "abc"
b = ["a", "b", "c"]
print "String {} po odwroceniu to : {}".format(a, odwroc(a))
print "Wartosci listy  {} po odwroceniu to : {} ".format(b, odwroc(b))
print koniec_zadania


'''
Zadanie 9:
 
Napisz funkcje, ktora zlicza wynik dla podanego wyrazu
Funkcja powinna dzialac dla duzych i malych liter
np. scrabble_score("AbC") tpowinna zwrocic 7 bo a = 1, b = 3, c = 3, 1 + 3 + 3 = 7
'''


def scrabble_score(string):
    score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
             "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
             "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
             "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
             "x": 8, "z": 10}
    string = string.lower()
    wynik = 0
    for char in string:
        wynik += score[char]
    return wynik

slowo = "AbC"
print "Za hardcodowane slowo {}, uzyskales liczbe punktow rowna : {}".format(slowo, scrabble_score(slowo))
print koniec_zadania

'''
Zadanie 10:
 
Napisz funkcje, ktora zwaraca mediane (wartos scrodkowa) z liczb podanych w liscie, czyli:
mediana([1,2,3,4,5])) powinna zwrocic: 3
 
Jezeli liczba cyfr na liscie jest parzysta to wez srednia ze srodkowych liczb
Uwaga! lista musi byc posortowana
 
Uwaga2: roznica miedzy python 2 a 3 w dzieleniu (3/2 daje 1, zamiast 1,5)
'''


def mediana(lista):
    lista.sort()
    if len(lista) < 2:
        return "something went horribly wrong"
    elif len(lista) % 2 == 0:
        print lista
        pozMe = (len(lista) + 1) / 2
        mediana = (lista[pozMe] + lista[pozMe + 1]) / 2
        mediana -= 0.5
        return mediana
    elif len(lista) % 2 != 0:
        print lista
        pozMe = (len(lista) + 1) / 2
        mediana = lista[pozMe - 1]
        return mediana
    else:
        return None

print mediana([1])
print "Mediana wynosi: {}".format(mediana([5, 3, 4, 2, 3, 3, 5, 5, 5, 4, 5]))
print "Mediana wynosi: {}".format(mediana([5, 3, 4, 3, 3, 5, 5, 5, 4, 5]))
print "Mediana wynosi: {}".format(mediana([1, 2, 3, 4, 5]))
print "Mediana wynosi: {}".format(mediana([2, 3, 2, 5, 2, 3, 2]))
print "Mediana wynosi: {}".format(mediana([1, 2, 1, 3, 1, 2, 1, 4]))
print koniec_zadania


'''
Zadanie 11:
 
Napisz funckje zamieniajaca slowo w tekscie ciagniem znakow ***, gdzie ilosc * to ilosc liter w zamienianym slowie
np.cenzura("moje slowo to najlepsze słowo", "slowo") powinno zwrocic "moje ***** to najlepsze ****"
'''


def cenzura(zdanie, slowo):
    result = re.sub(slowo, len(slowo) * "*", zdanie, flags=re.IGNORECASE)
    return result

zdanie = "moje slowo to najlepsze slowo"
slowo = "slowo"
print "Zwrocone zdanie to: {}, poniewaz wyraz: {}, zostalo poddane cenzurze".format(cenzura(zdanie, slowo), slowo)
print koniec_zadania

'''
Zadanie 12:
Napisz funkcję, która sprawdza czy podana liczba jest liczba pierwsza
np. czy_pierwsza(8) powinna zwrocic False, a czy_pierwsza(7) powinna zwrocic True
 
Pamietaj, wszystkie liczby mniejsze niz 2 nie sa liczba mi pierwszymi
'''


def czy_pierwsza(liczba):
    count = 0
    if liczba < 2:
        return False
    else:
        for x in range(1, liczba + 1):
            if liczba % x == 0:
                count += 1
    if count > 2:
        return False
    else:
        return True

a = 7
b = 8
print "Licznba {} jest liczba pierwsza ?".format(a, czy_pierwsza(a))
print "Licznba {} jest liczba pierwsza ?".format(b, czy_pierwsza(b))
print koniec_zadania

'''
Zadanie 13:
Zamien petle for na while; petla ma sprawdzac czy podana lista zawiera numer 33
 
data = [5, 33, 7, 12]
found = False
 
for n in data:
    if n == 33:
        found = True
 
if found:
    print("Lista zawiera 33")
else:
    print("lista nie zawiera 33")
'''

data = [5, 33, 7, 12]
szukana = 12
found = False
petla = len(data)
pos = 0

while petla > 0:
    if data[pos] == szukana:
        found = True
        break
    else:
        petla -= 1
        pos += 1

if found:
    print "Lista zawiera {}".format(szukana)
else:
    print "Lista nie zawiera {}".format(szukana)

print koniec_zadania

'''
Zadanie 14:
Napisz program, który operuje na słowniku wyrazów(odpowiedzi na pytania).
Przy uruchomieniu programu czekamy na pytanie i:
·        W przypadku znanego pytania wyświetlamy odpowiedz
·        Jak nasz program nie zna pytania to pytamy co mamy odpowiedzieć następnym razem i dodajemy odpowiedz do słownika
Zadanie zrobione w pliku personal_assistant.py
'''


