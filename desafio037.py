numero = int( input ('Digite o número que deseja converter: '))
escolha = int ( input ('Obrigado pela informação, agora escolha:\n 1 Para binário.\n 2 Para octal. \n 3 Para hexadecimal.'))
binario = numero % 2
if escolha == 1:
    while numero > 0:
        binario = ''
        print(binario)
        numero = numero //2
