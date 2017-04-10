'''
Zadanie nr 3
Napisz program, który pyta u¿ytkownika o konkretny katalog i podaje infomracje o jego rozmiarze.
'''

def get_size(path):
    total_size = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            print file
            print os.path.getsize(os.path.join(root, file))
            total_size += os.path.getsize(os.path.join(root, file))
    return str(total_size/1024) + " kb"

print get_size()