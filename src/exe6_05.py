'''
Exercício 5: Utilize o seguinte código em Python que guarda uma string:
str = 'X-DSPAM-Confidence:0.8475' 
Use a função find e o fatiamento destrings para extrair a porção da string depois do sinal de dois pontos e
use a função float para converter a string extraída em um número de ponto flutuante.
'''

str = 'X-DSPAM-Confidence:0.8475'
pos = str.find(':')
numero = float(str[pos+1:])
print(numero, type(numero))