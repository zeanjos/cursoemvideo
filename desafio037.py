while True:
    try:
        numero = int( input ('Digite o número que deseja converter: '))
        escolha = int ( input ('Obrigado pela informação, agora escolha:\n 1- Para binário.\n 2- Para octal. \n 3- Para hexadecimal.\n Digite: '))


        if escolha == 1:
            print('O número {} Convertido para binário é: {}'.format(numero, bin(numero)))
            break
        elif escolha == 2:
            print('O número{} Convertido para octal é: {}'.format(numero, oct(numero)))
            break
        elif escolha == 3:
            print('O número {} Convertido para hexadecimal é {}'.format(numero, hex(numero)))
            break
        else:
             print('Escolha incorreta! Tente novamente.')
    except ValueError:
            print('Escolha incorreta! Tente novamente.')