# -*- coding: utf-8 -*-
import os


'''
Zadanie nr 2
Napisz porgram, kt�ry przeskanuje podan� przez u�ytkownika lokalizacj� i przeskanuje ca�� jego struktutr� (wszystkie znajduj�ce sie w niej podkatalogi i pliki), zmieniaj�c nazwy wszytkich plik�w. Niech u�ytkownik zdecyduje jak te pliki maj� si� zmieni�: czy na ma�e lub du�e litery czy nazwy plik�w b�d� zaczyna� si� od du�ej litery
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
