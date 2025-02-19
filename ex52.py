tot = 0
num = int(input('Digite um número: '))
for c in range(1, num + 1):
    if num % c == 0:
        tot += 1
        print('O número é primo!')
        print('\033[33m', end='')
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end ='')
print('\n\033[m\nO número {} foi divisivel {} vezes,'.format(num, tot))
if tot == 2:
    print('\nO número {} é primo!'.format(num))
else:
    print('\nE por isso o número {} não é primo!'.format(num))
print('\033')