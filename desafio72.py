lista1 = (0, 1, 2, 3, 4,
           5, 6, 7, 8,
             9, 10, 11, 12,
               13, 14, 15, 16,
                    17, 18, 19, 20)
lista2 = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito',
             'nove', 'dez', 'onze', 'doze',
               'treze', 'quatorze', 'quinze', 'dezeseis',
                 'dezessete', 'dezoito', 'dezenove', 'vinte' )

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'Você digitou o número: {lista1[num]} E por extenso fica "{lista2[num]}"')
    else:
        print('Você digitou errado.')
        break

    desejo = str(input('Deseja continuar [S/N]: ')).lower().strip()
    if desejo == 's':
        print('Você escolheu continuar!')
        continue
    elif desejo == 'n':
        print('Você escolheu sair, até mais!')
        break
    else:
        print('Caracter invalido!')
       