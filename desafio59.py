

menu = None
maior = 0
while menu is None:
    num = float(input('Digite o seu número: '))
    num2 = float(input('Digite o seu número: '))
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
    if menu == 2:
        print(f'Os números digitados multiplicados dão resultado de: {mult:.2f}')
    if menu == 3:
        if num > num2:
            maior = num
        if num2 > num:
            maior = num2
        print(f'O maior número digitado é: {maior}')
