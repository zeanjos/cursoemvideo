from math import inf
from random import randint
maior = cont = 0
menor = inf
num_aleatorio = ()
while cont < 5:
    cont += 1
    aleatorio = randint(0, 20)
    num_aleatorio += aleatorio,
print('-='*20)
print(f'Os números gerados foram: {', '.join(str(x) for (x) in num_aleatorio)}')
print('-='*20)
print(f'O maior número entre os gerados é: {max(num_aleatorio)}')
print('-='*20)
print(f'O menor número entre os gerados é: {min(num_aleatorio)}')
print('-='*20)