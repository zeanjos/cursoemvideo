from random import randint
matriz = []

palpites = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'Sorteando {palpites} Jogos')

for p in range(palpites):
    jogo = []
    while len(jogo) < 6:
        numero = randint(0, 60)
        jogo.append(numero)
    matriz.append(jogo)

for indice, jogo in enumerate(matriz, start=1):
    jogo.sort()
    print(f'Jogo: {indice}: {jogo}')


