num = int(input('Digite o número que deseja fatorar: '))
c = num
f = 1
print(f'Calculando !{c} = ', end='')
for c in range(num, 0, -1):
    print(c, end='')
    print(' X ' if c > 1  else ' = ', end='')
    f *= c
    c -= 1   
print(f, end='')