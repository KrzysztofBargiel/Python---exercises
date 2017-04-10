# -*- coding: utf-8 -*-
import os

'''
Zadanie nr 1
Napisz porgram, który zapyta użytkownika o lokalizację i stworzy w niej nowy folder.
W nowo utworzonym folderze zostanie stworzony plik txt, w którym użytkownik będzie mógł wpisać dowolny tekst.
'''
directory_path = raw_input("Podaj sciezke gdzie mam utworzyc folder\n")
folder_name = raw_input("Podaj nazwe folderu:\n")
if directory_path[-1] != "\\":
    directory_path += "\\"
    print directory_path
if os.path.exists(directory_path + folder_name):
    print "Folder o podanej nazwie: {}, juz istnieje".format(folder_name)
if not os.path.exists(directory_path + folder_name):
    os.makedirs(directory_path + folder_name)
    file_name = raw_input("Jak juz mamy folder, dodaj jakis plik np .txt\n")
    file = open(directory_path + folder_name + '\\' + file_name, "a+")
    file.close()
