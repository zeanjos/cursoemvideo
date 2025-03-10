num = soma = cont = 0
while num < 999:
    num = int(input('Digite um número para somar, digite 999 se deseja parar: '))
    if num == 999:
        print('Você escolheu sair, até mais!')
        break
    elif num < 999:
            soma += num
    cont += 1
    print('-=-'*20)
print(f'O resultado da soma dos números digitado é de: {soma}, foram digitados {cont} números.')
print('-=-'*20)
    