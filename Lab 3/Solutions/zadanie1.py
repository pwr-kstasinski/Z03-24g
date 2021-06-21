import os
import sys
rootpath = (sys.argv[1])
(_, _, filenames) = os.walk(rootpath).next()
for f in filenames:
    if f.endswith(sys.argv[2]):
        print f