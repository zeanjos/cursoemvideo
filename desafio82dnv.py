numeros = []
impares = []
pares = []
continua = True
while continua:
    num = int(input('Digite um números, se desejar sair digite -1: '))
    if num < 0:
        print('Voce escolheu sair.')    
        continua = False
    else:
        numeros.append(num)
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
contagem_impar = len(impares)
contagem_par = len(pares)
numeros.sort()
pares.sort()
impares.sort()
print('-'*30 + '\n' +
f'Os números digitados foram {numeros}\n' +
    (f'Os números pares digitados são {pares}' if contagem_par > 0 else 'Não foi digitado nenhum numero par.') +
    (f'\nOs números impares digitados foram {impares}' if contagem_impar > 0 else 'Não foi digitado nenhum numero impar.'))