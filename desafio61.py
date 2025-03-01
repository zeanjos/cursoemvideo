p1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
while r <= p1:
    for i in range(p1, 11, r):
        print(f'Resultado: {i}')
    break
        