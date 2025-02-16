import random
print('-=-'*20)

aleatorio = random.choice([1, 2, 3])
jok = int(input('Digite a opção que deseja jogar do 1, 2 e 3: \n 1- Pedra\n 2- Papel\n 3- Tesoura\n :'))
if jok == 1:
    if aleatorio == 1:
        print('Você escolheu pedra, eu também escolhi pedra, empate!')
elif jok ==2:
    if aleatorio == 1:
        print('Eu escolhi papel e você pedra, eu ganhei!')
elif jok == 2:
    if jok == 2:
        print('Eu escolhi papel e você também, empate!')
elif jok == 1:
    if aleatorio == 2:
        print('Eu escolhi pedra e você papel, você ganhou!')
elif jok == 2:
    if aleatorio == 3:
        print('Eu escolhi papel e você tesoura, você ganhou!')
elif jok == 3:
    if aleatorio == 2:
        print('Eu escolhi tesoura e você papel, eu ganhei')
elif jok == 3:
    if aleatorio == 3:
        print('Eu escolhi tesoura e você também, empate!')
elif jok == 1:
    if aleatorio == 3:
        print('Eu escolhi pedra e você tesoura, eu ganhei!')
elif jok == 3:
    if aleatorio == 1:
        print('Eu escolhi tesoura e você pedra, você ganhou!')
        