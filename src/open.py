# Contando o númemro de linhas do arquivo
fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    count = count + 1
    
print('Line Count:', count)