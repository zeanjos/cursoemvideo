num = int(input('Digite um número: '))
for c in range(2, num):
    if num % c == 0:
        print('{} Não é primo.'.format(num))
    else:
        print('{} É um numero primo.'.format(num))