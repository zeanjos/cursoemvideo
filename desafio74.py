from random import randint
from math import inf

cont = 0
maior = 0
menor = inf
lista_vazia = () 
while cont < 5:
    cont += 1
    num_aleatorio = randint(1, 20)
    lista_vazia += (num_aleatorio, )
    if maior < num_aleatorio:
        maior = num_aleatorio
    elif menor > num_aleatorio:
        menor = num_aleatorio
print('''Os valores sorteados foram:''', *lista_vazia, 
f'''\nO maior valor é {maior} e o menor é {menor}''')