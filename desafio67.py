n = 0
calc = 1
while True:
    print('-'*50)
    n = int(input('Digite o número que deseja saber a tabuada:'))
    print('-'*50)
    if n < 0:
        print('Você digitou um número negativo e resolveu parar. Até mais!')
        break
    for c in range(1, 11):
        calc = n * c
        print(f'{n} x {c} = {calc}')