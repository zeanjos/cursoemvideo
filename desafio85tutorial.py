num = [[], []]
valores = 0
for c in range(1, 8):
    valores = int(input(f'Digite o {c}º Valor: '))
    if valores % 2 == 0:
        num[0].append(valores)
    else:
        num[1].append(valores)
num[0].sort()
num[1].sort()
print('-'*30)
print(f'Todos os valores: {num}\nOs valores pares digitados foram: {num[0]} e os impares: {num[1]}')
print('-'*30)