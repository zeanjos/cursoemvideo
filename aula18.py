galera = []
dado = []
tot_maior = tot_menor = 0
for c in range(0, 3):
    print('-'*30)
    dado.append(str(input('Digite o seu nome: ')))
    print('-'*30)
    dado.append(int(input('Digite sua idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        tot_maior += 1
        print(f'{p[0]} É maior de idade.')
    else:
        print(f'{p[0]} É menor de idade')
        tot_menor +=1
print('-'*30)
print(f'O número de pessoas maiores de 21 anos é {tot_maior}, e o total de menores de 21 anos é {tot_menor}')
print('-'*30)