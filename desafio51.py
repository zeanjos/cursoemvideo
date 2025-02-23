p1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
res = p1
for c in range(1, 11):
    print('O termo: {}, razão de: {} Valor {}'.format(c, r, res))
    res += r