
soma = 0
num = 0
while num < 999:
    num = int(input('Digite um número para somar, digite 999 se deseja parar: '))
    if num == 999:
        print('Você escolheu sair, até mais!')
        break
    elif num < 999:
            soma += num
    print('-=-'*20)
print(f'O resultado da soma dos números digitado é de: {soma}')
print('-=-'*20)
    