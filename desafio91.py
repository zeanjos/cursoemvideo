from random import randint
jogador1 = jogador2 = jogador3 = jogador4 = 0
lista = {}

for c in range(1,5):
    lista[c] = randint(0, 100)

for jogador, valor in lista.items():
    print(f'O jogador {jogador} tirou {valor}')
    