'''
Exercício 1: Escreva um loop while que inicia no último caractere da
string e caminha para o primeiro caractere, imprimindo cada letra em
uma linha separada.
'''
fruta = 'banana'
indice = len(fruta)-1
print(indice)

while indice >= 0:
    letra = fruta[indice]
    print(letra)
    indice = indice-1
    
    


