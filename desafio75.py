cont = 0
cont_nove = 0
valores = str()
primeiro_tres = 0
qntd = 0
while cont < 4:
        num = int(input('Digite um número: '))
        num_str = str(num)
        cont += 1
        valores += num_str + ', '
        cont_nove += num_str.count('9')

        try:
            num_f = int(num_str.index('3'))
        except ValueError:
              print('Não possui numero 3')
        else:
            print(num_f)
            if primeiro_tres == 0:
                  primeiro_tres = num_f
                  ind_pri_tres = cont
        
            
        


print(f'Valores: {valores} \nQuantidade de vezes que o 9 apareceu: ', cont_nove, f'\nO primeiro número três apareceu em indice:{ind_pri_tres}')