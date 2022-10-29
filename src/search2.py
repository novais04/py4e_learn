'''
consultado só os emails do arquivo mbox-short.txt
'''
'''
rstrip method which tira os espaços em branco do lado direito da
stirng, como pode ser observado:
'''
fhand = open('mbox-short.txt')
for line in fhand:
    line  = line.rstrip()
    if line.startswith('From:'):
        print(line)
#scr/search2.py