from random import randint
from time import sleep
matriz = []

palpites = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'\nSorteando {palpites} Jogos!')
print('-'*30)

for p in range(palpites):
    jogo = []
    while len(jogo) < 6:
        numero = randint(0, 60)
        jogo.append(numero)
    matriz.append(jogo)

for indice, jogo in enumerate(matriz, start=1):
    jogo.sort()
    print(f'Jogo: {indice}: {jogo}')
    sleep(1)
print('-'*10, 'Boa sorte!', '-'*10)

