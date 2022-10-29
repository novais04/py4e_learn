# Use the file name mbox-short.txt as the file name
fname = input("Digite o nome do aquivo: ")
fhand = open(fname)
count = 0
flt_tot = 0
for line in fhand:
    line = line.rstrip()# remove qualquer carcter especial no fim da string
    if line.find('X-DSPAM-Confidence:') == -1 :
        continue
    pontos = line.find(':')
    flt = float(line[pontos+1:])
    flt_tot = flt_tot + flt
    count = count + 1
print(f"Average spam confidence: {flt_tot/count}")git 