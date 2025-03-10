print('-=-'*14)
n = int(input('Digite quantos números você quer mostrar: '))
print('-=-'*14)
t1 = 0
t2 = 1
cont = 3
while cont < n:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print(f'{t3} --> ', end='')
    cont += 1
print('Fim!')

