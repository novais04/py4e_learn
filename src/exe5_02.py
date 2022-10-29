'''
Exercício 2: Escreva outro programa que pede por uma lista de números
como mostrada acima e mostra, no final, o máximo e o mínimo dos
números ao invés da média.
'''
list = list()
count= 0
soma = 0
while True:
    inp = input("Digite um número: ")
    if inp == "done":
        break
    try:
        valor = int(inp)
    except:
        print("Invalid input")
        continue
    list.append(valor)
    soma = soma + valor
    count += 1
    
print(f'Maximum is {max(list)}')
print(f'Minimum is {min(list)}')