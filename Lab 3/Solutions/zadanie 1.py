import glob
import os

path = input("Podaj sciezke: ")
ext = input("podaj rozszerzenie pliku: ")

direction = path + "*." + ext
for f in glob.glob(direction):
    (filepath, filename) = os.path.split(f)
    print(filename)
