# -*- coding: utf-8 -*-
import os


'''
Zadanie nr 2
Napisz porgram, który przeskanuje podan¹ przez u¿ytkownika lokalizacjê i przeskanuje ca³¹ jego struktutrê (wszystkie znajduj¹ce sie w niej podkatalogi i pliki), zmieniaj¹c nazwy wszytkich plików. Niech u¿ytkownik zdecyduje jak te pliki maj¹ siê zmieniæ: czy na ma³e lub du¿e litery czy nazwy plików bêd¹ zaczynaæ siê od du¿ej litery
'''
directory_path = raw_input("Podaj sciezke ktora masz przeskanowac\n")

if directory_path[-1] != "\\":
    directory_path += "\\"
os.chdir(directory_path)
print "Orginalna struktura wyglada nastepujaco"
print "---------------------------------------"
for root, dirs, files in os.walk(directory_path):
    for file in files:
        print(root, file)
job = raw_input("Mozesz zmienic nazwe plikow, zamieniajace je na duze znaki / male znaki / pierwsza znak z duzej, wpisz odpowiednio (U/L/C)\n")[0].upper()
for root, dirs, files in os.walk(directory_path):
    for dir in dirs:
        if job == "L":
            os.rename(os.path.join(root, dir), os.path.join(root, dir.lower()))
        elif job == "U":
            os.rename(os.path.join(root, dir), os.path.join(root, dir.upper()))
        elif job == "C":
            os.rename(os.path.join(root, dir), os.path.join(root, dir.capitalize()))
        else:
            print "Wprowadzono nie poprawna komende"
            break
    for file in files:
        if job == "L":
            os.rename(os.path.join(root, file), os.path.join(root, file.lower()))
        elif job == "U":
            os.rename(os.path.join(root, file), os.path.join(root, file.upper()))
        elif job == "C":
            os.rename(os.path.join(root, file), os.path.join(root, file.capitalize()))
        else:
            break
print "Zmieniona struktura wyglada nastepujaco"
print "---------------------------------------"
for root, dirs, files in os.walk(directory_path):
    for file in files:
        print(root, file)
