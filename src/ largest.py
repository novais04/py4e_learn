'''
Repetições máximas e mínimas

Para achar o máximo valor em uma lista ou sequência, construímos a seguinte
repetição:
'''

maximo = None
print(f"Antes: {maximo}")
for itervar in [3, 41, 12, 9, 74, 15]:
    if maximo is None or itervar > maximo:
        maximo = itervar
    print(f"Laço: {itervar} {maximo}")
print(f"Máximo: {maximo}")
