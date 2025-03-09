
p1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
s = p1
total = 0
mais = 10
cont = 1
while mais != 0:
    total = total + mais
    while cont <= total:
            print(f'{s} --> ', end='')
            s += r
            cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais: '))
print(f'Progressão finalizada com {cont} termos exibidos.')
    
print('FIM')
