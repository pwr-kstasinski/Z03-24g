
import glob

directory = input("Enter directory :")

extension = input("Enter file extension:")

print(glob.glob(f'{directory}\*.{extension}'))
