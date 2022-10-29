
# Exercicio 4: Baixe a copia do arquivo www.py4e.com/code3/romeo.txt.
# Escreva um programa para abrir o arquivo chamado romeo.txt e leia-o linha por
# linha. Para cada linha, separe-a em uma lista de palavras usando a função split.
#Para cada palavra, cheque se esta palavra já existe na lista. Caso não exista,
#adicione ela. Quando o programa terminar de verificar, ordene e imprima estas
#palavras em ordem alfabética.**

#Enter file name: romeo.txt
#['Arise', 'But', 'It', 'Juliet', 'Who', 'already',
#'and', 'breaks', 'east', 'envious', 'fair', 'grief',
#'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft',
#'sun', 'the', 'through', 'what', 'window',
#'with', 'yonder']


# metodos usados
# Metodo 01 - O método rstrip() remove quaisquer caracteres finais (caracteres no final de uma string), 
# espaço é o caractere final padrão a ser removido.

# O método split() divide uma string em uma lista.

list = list()

fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    line =line.rstrip() # metodo 01
    words= line.split() # metodo 02
    for word in words:
        if word in list:
            continue
        list.append(word)
        list.sort()

print(list)
    