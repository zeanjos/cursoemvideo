p1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
s = p1
cont = 1
while cont <=10:
    for i in range(p1, 11):
        s += r
        cont += 1
        print(f'{s}', end='')
        if cont <= 10:
            print(' -> ', end='')
        else:
            print('\nFim!')
        break
    


        