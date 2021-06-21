import os,sys

if len(sys.argv)>2:
	ext = sys.argv[1]
	path = sys.argv[2]
else:
	ext = input("Enter extension: ")
	path = input("Enter path: ")

for f in os.listdir(path):
	if f.endswith(ext):
		print(f)