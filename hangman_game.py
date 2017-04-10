'''
Komputer losuje slowo (mozemy zadeklarowac na sztywno, mozemy pobierac z jakiegos pliku, moze podawac inny gracz)
Uzytkownik musi odgadnac slowo.
W kazdej turze uzytkownik podaje jedna litere.
Jezeli litera znajduje sie w odgadywanym slowne, program wyswietla opdoiwedni komunikat, wyswietla slowo z odszyfrowana litera (pozostale litery sa zaszyfrowane). Gracz wygrywa jezeli odgadnie cale slowo
Jezeli litera nie znajduje sie w odgadywanym slowie, program wyswietla odpowiedmni komunikat wraz z rysunkiem wiszacego ludzika oraz podaje listre liter juz uzytych podczas zgadywania.
Rysnek szubienicy z kazda nietrafiona litera ma sie zmieniac. W ostatniej turze - kiedy pojawi sie ostani rysnek - gracz przegrywa gre.

'''
from szubienica_images import *
import random

path = r'C:\Users\bargikrz\PycharmProjects\szubienica\slowa.txt'
turn = 6
count_tries = 1
miss = []



def upload_word(path):
    fn = open(path, "a+")
    fn = fn.readlines()
    count = len(fn)
    upload = fn[random.randint(0, count-1)]
    return list(upload.lower().strip())

def hashtag_word(upload):
    word = upload
    coded = len(word) * "-"
    return list(coded)

word = upload_word(path)
hashtag = hashtag_word(word)


print word
print "Witaj w grze Szubienica\n"
print "Zostalo wylosowane imie, ktore musisz odgadnac, wiec... zaczynajmy"

while turn > 0:

    quess = raw_input("Podaj litere\n")[0]
    occurs = False
    if quess in hashtag:
        print "Podales juz litere {} wczesniej, wybierz inna".format(quess)
        continue
    for i in range(0, len(word)):
        if quess == word[i]:
            print "Litera {} znajduje sie na {} miejscu ".format(quess, i + 1)
            hashtag[i] = word[i]
            miss.append(quess)
            occurs = True
    if occurs == False:
        print "Podana litera {}, nie znajduje sie w szukanym slowie".format(quess)
        print tries['fail_{}'.format(count_tries)]
        miss.append(quess)
        count_tries += 1
        turn -= 1
        if turn == 0:
            print "koniec, przegrales !!!"
            break
    if "-" not in hashtag:
        print "koniec, wygrales, szukane imie to {} !!!".format("".join(word))
        break

    # print "######"
    # print str.join("", word)
    print "".join(hashtag)
    print "Podane litery to {}".format(list(set(miss)))
