print('='*20)
ced = 50
t_ced = 0

while True:
    try:
        valor = float(input('Digite o valor que deseja sacar R$: '))
    except ValueError:
        print('Você digitou incorretamente, digite novamente.')
    total = valor
    cont_cinq = cont_vin = cont_cin = cont_um = cont_cinq = 0
    while True:
        if total >= ced:
            total -= ced
            cont_cinq += 1
            t_ced += 1
        else:
            print(f'Total de cédulas {t_ced} de R$ {ced}')
            if ced == 50:
                ced = 20
            elif ced == 20:
                ced = 10
            elif ced == 10:
                ced = 5
            elif ced == 5:
                ced = 1
            t_ced = 0
            if total == 0:
                
                break
            desejo = str(input('Deseja continuar [S/N]? ')).strip().lower()[0]
            while desejo != 's' and desejo != 'n':
                print('Opção invalida, digite novamente.')
                desejo = str(input('Deseja continuar [S/N]? '))     
            if desejo == 'n':
                print('Você escolheu sair!')
                break
            if desejo == 's':
                print('Você escolheu continuar!')
                
                
        
