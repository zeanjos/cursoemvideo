from random import randint
matriz = []

palpites = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'Sorteando {palpites} Jogos')
for p in range(palpites):
    jogo = []
    matriz.append(jogo)
    for i in range(6):
        jogo.append(randint(0, 60))

print(matriz)
