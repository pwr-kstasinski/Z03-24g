
from pathlib import Path

path1 = str(input("Enter path"))
extension = str(input("Enter extension"))
extension = "*."+ extension
for path in Path(path1).rglob(extension):
    print(path.name)