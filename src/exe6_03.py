
def contagem(palavra, letra):
    '''
    Conta o número de vezes que uma determinada letra aparece em uma palavra
    Entrada: palavra -- a palavra em questão
             letra -- a letra na palavra a ser contada
    Saída: imprime o número de letras
    '''
    counter = 0
    
    for caracter in palavra:
        if caracter == letra:
            counter = counter + 1
    print(counter)

input_palavra= input("Entre com a Palavra: ")
input_letra = input("Entre com a Letra: ")
contagem(input_palavra, input_letra)

