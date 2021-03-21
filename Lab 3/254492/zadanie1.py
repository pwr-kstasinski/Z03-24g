import fnmatch
import os
import sys

files = (fnmatch.filter(os.listdir(sys.argv[1]), "*" + sys.argv[2]))
for x in files:
    print(x)
