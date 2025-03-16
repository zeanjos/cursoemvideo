from random import randint
 

jogador = 0
cont = 0

while True:
    num = randint(1, 10)
    jogador = int(input('Digite um número par ou impar no range de 1 a 10: '))
    if jogador == 999:
        print('Você escolheu sair, até mais!')
        break
    soma = jogador + num
    parouim = str(input('Par ou impar [P/I]: ')).strip().lower()[0]
    if soma % 2 == 0 and parouim == 'p':
        print(f'A soma de {jogador} e {num} dão resultado {soma} Um número par, você ganhou! Sua sequência foi de {'Vitória' if cont == 1 else 'Vitórias'}')
    elif soma % 2 == 1 and parouim == 'i':
        cont += 1
        print(f'A soma de {jogador} e {num} Dão resultado {soma} Um número impar, você ganhou! Sua sequência foi de {'Vitória' if cont == 1 else 'Vitórias'    }')
    elif soma % 2 == 0 and parouim == 'i':
        cont += 1
        print(f'A soma de {jogador} e {num} Dão resultado {soma} Um número par, você escolheu um número impar, você perdeu! Sua sequência foi de {'Vitória' if cont <= 1 else 'Vitórias'}.')
    elif soma % 2 == 1 and parouim == 'p':
        print(f'A soma de {jogador} e {num} Dão resultado {soma} Um número impar, você escolheu um número par, você perdeu! Sua sequência foi de {'Vitória' if cont <= 1 else 'Vitórias'}')
    