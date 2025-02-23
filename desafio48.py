soma = 0
for c in range(1, 501):
    if c % 2 == 1:
        if c % 3 == 0:
            soma += c
            print('Número impar multiplo de 3: {}'.format(c))
print('Soma total: {}'.format(soma))