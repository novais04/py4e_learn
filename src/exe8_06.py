'''
Exercício 6: Reescreva o programa que solicita o usuário uma lista de
números e prints e imprime em tela o maior número e o menor número
quando o usuário digitar a palavra “feito”. Escreva um programa para
armazenar as entradas do usuário em uma lista e use as funções max()
e min() para computar o número máximo e o mínimo depois que o laço
for completo.
Digite um número:
Digite um número:
Digite um número:
Digite um número:
Digite um número:
Digite um número:
Máximo: 9.0
Mínimo: 2.0
'''

def middle(t):
    del t[1:len(t)-1]
    return(t)

numlist = list()
while(True):
    inp = input("Digite um número (feito p/ sair): ")
    if inp == "feito":
        break
    num = float(inp)
    numlist.append(num)
    
max_num = max(numlist)
min_num = min(numlist)

print(f"Máximo: {max_num} \nMínimo: {min_num}")
    