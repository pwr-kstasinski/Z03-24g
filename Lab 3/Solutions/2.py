import os,sys,subprocess

path = sys.argv[1] if len(sys.argv)>0 else input("Enter path: ")
proc = subprocess.Popen("tree %s" % path, stdout=subprocess.PIPE, shell=True, encoding="cp852")
(tree,_) = proc.communicate()
tree = tree.split("\n",3)[-1]
print(path)
print(tree)