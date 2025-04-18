from random import randint
from time import sleep
lista = []
jogos = []

print('-'*30)
palpite = int(input('Quantos jogos você quer que eu sorteie? '))
total = 0
while total <= palpite:
    contador = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            contador += 1
        if contador >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    print(f'Os números sorteados foram: {jogos}')
