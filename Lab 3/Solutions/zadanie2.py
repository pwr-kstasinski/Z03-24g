import os
import sys
rootpath = (sys.argv[1])
lenOfRoot = len(rootpath.split('\\'))
for dirpath, dirs, files in os.walk(rootpath):
	path = dirpath.split('\\')
	print (len(path) - lenOfRoot)*'|   '+'|---',  os.path.basename(dirpath)
	for f in files:
		print (1+len(path)-lenOfRoot)*'|   '+'|---', f