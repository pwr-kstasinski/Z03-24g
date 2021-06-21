import glob, os
print("Podaj sciezke: ")
path = input()
os.listdir(path)
for file in glob.glob("*.txt"):
    print(file)
#D:\Politechnika-Wrocławska\Laboratoria\JezykiSkryptowe\Lista3\PrototypyLubTesty