class TV:
    '''
    Klasa telewizor
    '''

    def __init__(self, marka, model, rok, kanal = 1, vol = 1):
        print "wyprodukowano nowy telewizor"
        self.marka = marka
        self.model = model
        self.rok = rok
        self.kanal = kanal
        self.vol = vol


    def kanal(self, channel):
        if channel == 1:
            self.kanal += 1
            print "Obecny kanal {}".format(self.kanal)
        elif channel == 0:
            self.kanal -= 1
            print "Obecny kanal {}".format(self.kanal)

    def enter_kanal(self, channel):
        if int(channel) < 1 or int(channel) > 99:
             print "Nie ma takiego kanalu"
        else:
            print "Wybrano kanal {}".format(int(channel))
            self.kanal = channel

    def glosnosc(self, glosnosc):
        if glosnosc == 0:
            self.vol -= 1
            print "Poziom glosnosci {}".format(self.vol)
        elif glosnosc == 1:
            self.vol += 1
            print "Poziom glosnosci {}".format(self.vol)
        else:
            print "Error"


power = True
Telewizor = TV("Samsung", "KS7000" ,"2017")
while power :
    print("""
    Witaj w trybie manualnego pilota {} {} z {} :
    1 - VOL UP
    2 - VOL DOWN
    3 - CHANNEL UP
    4 - CHANNEL DOWN 
    5 - ENTER CHANNEL
    6 - TURN OFF 
    """).format(Telewizor.marka, Telewizor.model, Telewizor.rok)

    wybor = int(raw_input("Podaj numer:\n"))
    if wybor == 1:
        Telewizor.glosnosc(1)
    elif wybor == 2:
        Telewizor.glosnosc(0)
    elif wybor == 3:
        Telewizor.kanal(1)
    elif wybor == 4:
        Telewizor.kanal(0)
    elif wybor == 5:
        number = raw_input("Podaj numer kanalu: ")
        Telewizor.enter_kanal(number)
    elif wybor == 6:
        print "Telewizor wylaczony"
        break
