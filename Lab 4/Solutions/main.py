import sya

exp = input("Enter expression: ")
r = sya.parse(exp)
r.calc(sya.OPDICT)
r.display()