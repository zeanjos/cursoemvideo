n = int(input('Digite o número que deseja fatorar: '))
c = n
f = 1
print(f'Calculando !{n} = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' X ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)
    #c -= 1
#s = n * c
#s *= c
#print(f'{n} x {c} = {s}')##

