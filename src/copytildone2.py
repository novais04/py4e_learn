'''
Aqui está um exemplo de laço que copia as entradas do usuário até ele digitar
“pronto”, mas considera as linhas que começam com o caractere cerquilha (#)
como linhas que não devem ser exibidas (como os comentários em Python).
'''
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'pronto':
        break
    print(line)
print('pronto!')
    