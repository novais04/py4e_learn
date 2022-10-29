'''
Por exemplo, suponha que você queira entradas do usuário até que ele digite
pronto. Você pode escrever:
'''
while True:
    line = input("> ")
    if line == 'pronto':
        break
    print(line)
print('pronto')