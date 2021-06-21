import os
import sys

 files = os.listdir("dir")
 for file in files:
    if file.endswith(".txt"):
      print(file)

