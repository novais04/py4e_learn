'''
Exercício 1: Escreva um programa que lê repetitivamente números até
que o usuário digite “pronto”. Quando “pronto” for digitado, mostre a
soma total, a quantidade e a média dos números digitados. Se o usuário
digitar qualquer coisa que não seja um número, detecte o erro usando
o trye o except e mostre na tela uma mensagem de erro e pule para o
próximo número.

output:
Digite um número: 4
Digite um número: 5
Digite um número: dado errado
Entrada Inválida
Digite um número: 7
Digite um número: pronto
16 3 5.333333333333333

'''

count= 0
soma = 0
while True:
    inp = input("Digite um número: ")
    if inp == "pronto":
        break
    try:
        valor = float(inp)
    except:
        print("Por favor, entre com um número")
        continue
    soma = soma + valor
    count += 1
    
print(f"{soma} - {count} - {soma/count}")


    