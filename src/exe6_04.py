
''' 
**Exercício 4: Existe um método na string chamado count que é similar à função
usada no exercício anterior. Leia a documentação desse método em:

![string](https://docs.python.org/library/stdtypes.html#string-methods)

Escreva uma invocação que conta o número de vezes que a letra “a” aparece em
“banana”.**
'''

def contagem(palavra, letra):
    '''
    Conta o número de vezes que uma determinada letra aparece em uma palavra
    Entrada: palavra -- a palavra em questão
             letra -- a letra na palavra a ser contada
    Saída: imprime o número de letras
    '''
    cont = palavra.count(letra)
    print(cont)

input_palavra= input("Entre com a Palavra: ")
input_letra = input("Entre com a Letra: ")
contagem(input_palavra, input_letra)

