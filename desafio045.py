import random
print('-=-'*20)

aleatorio = random.choice([1, 2, 3])
jok = int(input('Digite a opção que deseja jogar do 1, 2 e 3: \n 1- Pedra\n 2- Papel\n 3- Tesoura\n :'))
if jok == 1:
    if aleatorio == 1:
        print('Você escolheu pedra, eu também escolhi pedra, empate!')
elif jok ==2:
    if aleatorio


