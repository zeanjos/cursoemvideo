cont = 0
cont_nove = 0
valores = str()

while cont < 4:
    try:

        num = int(input('Digite um número: '))
        num_str = str(num)
        cont += 1
        valores += num_str + ', '
        cont_nove += num_str.count('9')
    except ValueError:
        print('Digito invalido, digite novamente.')


print(f'Valores: {valores} Quantidade de vezes que o 9 apareceu: ', cont_nove)