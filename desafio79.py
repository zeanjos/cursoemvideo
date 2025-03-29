
numeros = []
indice = 0
continuar = True
while continuar:
    for i in range(0, indice + 1):
        print('-'*30)
        num = int(input('Digite um número: '))
        print('-'*30)
        numeros.append(num)

        desejo = str(input('Deseja continuar [S/N] ?')).lower().strip()
        if desejo == 's':
            print('Você escolheu continuar!')
        elif desejo == 'n':
            print('Você escolheu sair!')
            continuar = False
      
            
        
        
    
