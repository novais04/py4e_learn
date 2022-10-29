'''
O método split é muito eficaz quando se depara com esse tipo de problema. 
    Podemos escrever um pequeno programa que procure por linhas onde a linha comece com  “From”, 
    `split` essas linhas e, em seguida, imprima a terceira palavra na linha:
'''
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    print(words[2])