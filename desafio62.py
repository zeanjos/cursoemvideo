
p1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
while r <= 10:
    for i in range(p1, 11, r):
        print(f'Resultado: {i}\n')
    desejo = int(input('Deseja continuar? [0] Não [1] Sim '))
    if desejo == 0:
        print('Você escolheu sair, até mais!')
        break