from random import randint
cont = 0
aleatorio = randint(1, 10)
acertou = False
print('''Estou pensando em um número de 1 a 10...\n
Consegue adivinhar qual foi?''')
while not acertou:
    cont += 1
    print('-=-'*14)
    palpite = int(input('Digite seu palpite: '))
    if palpite == aleatorio:
        acertou = True
        print(f'Você acertou! Foram {cont} tentativas.')
        print('-=-'*14)
    else:
        if palpite < aleatorio:
            print('É um número maior! Você errou, tente novamente.')
        elif palpite > aleatorio:
            print('É um numero menor! Você errou, tente novamente.')
        