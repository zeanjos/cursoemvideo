numeros = []
par = []
impar = []
continua = True
while continua:
    num = int(input('Digite um número, ou digite -1 se desejar parar: '))
    if num == -1:
        print('-'*30)
        print('Voce escolheu parar.')
        continua = False
    else:
        numeros.append(num)
        if num % 2 == 0:
            par.append(num)
        elif num % 2 != 0:
            impar.append(num)
        quantia = len(numeros)
        numeros.sort()
print(f'A lista completa é {numeros} Foi digitado {par} Numerações par,'
      f'{impar} impar e no total {quantia} Numerações')
print('-'*30)
