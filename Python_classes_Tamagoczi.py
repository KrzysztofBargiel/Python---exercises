

'''
Zadanie 1.
Ulepsz program Opiekun zwierzaka, pozwalajac uzytkownikowi na okreslenie ilosci pozywienia podawanego zwierzakowi i ilosci zabawek.

'''

class Zwierzak():
    "to jest zwierzak, ktorego trzeba karmic i bawic sie z nim"

    def __init__(self, imie, nuda = 0, glod = 0, zmeczenie = 0 ):
        print("rodzi sie nowy zwierzak")
        self.imie = imie
        self.nuda = nuda
        self.glod = glod
        self.zmeczenie = zmeczenie

    def mowi(self):
        print("Jestem {} i jestem {}".format(self.imie, self.nastroj))
        self.__starzenie()

    def zabawa(self):
        print("Jeee zabawa!")
        print("""
        Lalka ( -3 nuda, +1 zmeczenie )
        Auto ( -4 nuda, +1 zmeczenie )
        GameBoy ( -6 nuda, +2 zmeczenie )
        Pilka ( -10 nuda, +4 zmeczenie )
        """)
        wybor = raw_input("Wybierz zabawke\n").lower().strip()
        if wybor == "lalka":
            nuda = 3
            zmeczenie = 1
        elif wybor == "auto":
            nuda = 4
            zmeczenie = 1
        elif wybor == "gameboy":
            nuda = 6
            zmeczenie = 2
        elif wybor == "pilka":
            nuda = 10
            zmeczenie = 4
        else:
            print "Zly wybor"
            nuda = 0
            zmeczenie = 0
        if nuda != 0:
            print "{} jest szczesliwy, bawi sie i skacze, znudzenie spada o 4 punkty procentowe  i wynosi {}".format(imie, self.nuda)
        self.nuda -= nuda
        self.zmeczenie += zmeczenie
        if self.nuda < 0:
            self.nuda = 0
        self.__starzenie()


    def je(self):
        print("Omniomniom Co jemy? ")
        print("""
        Ciastko ( -3 glod, +1 zmeczenie )
        Kanapka ( -4 glod, +1 zmeczenie )
        Pizza ( -6 glod, +2 zmeczenie )
        Tort ( -10 glod, +4 zmeczenie )
        """)
        wybor = raw_input("Co dajemy do jedzenia, podaj nazwe\n").lower().strip()
        if wybor == "ciastko":
            jedzenie = 3
            zmeczenie = 1
        elif wybor == "kanapka":
            jedzenie = 4
            zmeczenie = 1
        elif wybor == "pizza":
            jedzenie = 6
            zmeczenie = 2
        elif wybor == "tort":
            jedzenie = 10
            zmeczenie = 4
        else:
            print "Tego nie ma w menu"
            jedzenie = 0
            zmeczenie = 0

        self.glod -= jedzenie
        self.zmeczenie += zmeczenie
        if self.glod < 0:
            self.glod = 0
        if zmeczenie != 0:
            print "{} cieszy sie jak glupi, do jedzenie dostal {}, glod zostal zreduowany o {} i na chwile obecna wynosi {}, zmeczenie jest na poziomie {} ".format(imie, wybor, jedzenie, self.glod, self.zmeczenie)

    def __starzenie(self):
        self.nuda += 1
        self.glod += 1

    def spanie(self):
        self.zmeczenie -= 15
        if self.zmeczenie < 0:
            self.zmeczenie = 0
        print "{} zamyka oczy i idzie spokojnie spac, poziom zmeczenia spada o 15 punktow i wynosi {}".format(imie, self.zmeczenie)
    @property
    def nastroj(self):
        nieszczesliwy = self.glod + self.nuda
        if nieszczesliwy < 5:
            result = "szczesliwy"
        elif 5 <= nieszczesliwy <= 10:
            result = "neutralny"
        elif 11 <= nieszczesliwy <= 15:
            result = "smutny"
        else:
            result = "wsciekly!"
        return result

imie = raw_input("Jak ma sie nazywac zwierzak?\n")
zwierz1 = Zwierzak(imie)

gra = True

while gra:
    print("""
    Opiekuj sie zwierzakiem
    0 - zakoncz gre
    1 - posluchaj zwierzaka
    2 - nakarm zwierzaka
    3 - spanie
    4 - pobaw sie ze zwierzakiem
    """)

    wybor = raw_input("Co wybierasz?\n")

    if wybor == "0":
        print("Konczymy gre")
        gra = False

    elif wybor == "1":
        zwierz1.mowi()

    elif wybor == "2":
        zwierz1.je()

    elif wybor == "3":
        zwierz1.spanie()

    elif wybor == "4":
        zwierz1.zabawa()

    else:
        print("niewlasciwy wybor, wybierz jeszcze raz")

