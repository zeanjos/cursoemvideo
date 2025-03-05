

menu = None
maior = 0
while menu != 5:
    num = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    s = num + num2
    mult = num * num2
    
    menu = int(input('''Digite um valor para realizar as operações matemáticas:\n
[1] Somar\n
[2] Multiplicar\n
[3] Maior\n
[4] Novos números\n
[5] Sair do programa.\n
Digite a opção desejada: '''))
    
    if menu == 1:
        print(f'Os números digitados somados dão resultado de: {s:.2f}')
        desejo = str(input('Deseja continuar? [S/N]: ')).lower()  # noqa: F821
    if desejo == 'n':  # noqa: F821
        print('Você escolheu sair, tchau!')
    elif menu == 2:
        print(f'Os números digitados multiplicados dão resultado de: {mult:.2f}')
    elif menu == 3:
        if num > num2:
            maior = num
        if num2 > num:
            maior = num2
            print(f'O maior número digitado é: {maior}')
        desejo = str(input('Deseja continuar? [S/N]: ')).lower()
        if desejo == 'n':
            print('Você escolheu sair, tchau!')
        if num == num2:
            print('Os valores são iguais, não existe maior.')
        desejo = str(input('Deseja continuar? [S/N]: ')).lower()
        if desejo == 'n':
            print('Você escolheu sair, tchau!')
            break
        elif desejo == 's':
            print('Continuando...\n')
    elif menu == 4:
        print('Você escolheu digitar novos números, boa jornada.')
    elif menu == 5:
        print('-=-'*16)
        print('Opção 5 escolhida, até mais!')
        print('-=-'*16)
    else:
        print('Opção invalida!')
        
