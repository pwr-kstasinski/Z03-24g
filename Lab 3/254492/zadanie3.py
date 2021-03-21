import sys

numberlist = [0] * (len(sys.argv) - 1)
for x in range(0, len(sys.argv) - 1):
    numberlist[x] = int(sys.argv[x+1])
print(numberlist)
numberlist.sort()
for x in numberlist:
    print(str(x) + " ", end="")
