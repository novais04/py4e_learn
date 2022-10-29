'''
Escreva uma função chamada `chop` que pega uma lista e a modifica, 
removendo o primeiro e o último elemento, e retorna None. 
Em seguida, escreva uma função chamada middle que recebe uma lista e 
retorna uma nova lista que contém todos os elementos, 
exceto o primeiro e o último.
'''

def chop(t):
    t.pop(0)
    t.pop(len(t)-1)
    return(t)

def middle(t):
    del t[1:len(t)-1]
    return(t)
    
t = [0,2,3,4,5]

chop = chop(t)
print(f"chop: {chop}")

t = [0,2,3,4,5]
middle = middle(t)
print(f"me: {middle}")

