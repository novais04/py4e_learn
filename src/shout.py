"""
    usando try/except
"""
print("python shout.py")
fname = input("Dogite o nome do aquivo: ")
fhand = open(fname)

for line in fhand:
    line = line.rstrip()
    print(line.upper())
