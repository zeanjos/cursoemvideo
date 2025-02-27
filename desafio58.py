from random import randint

cont = 1
aleatorio = randint(1, 10)
escolha = int(input('Digite um número de 1 a 10 e tente adivinhar: '))
if escolha == aleatorio:
    print(f'Você acertou de primeira.')
else:
    print('Você errou, tente novamente.')
    cont += 1
while escolha != aleatorio:
    cont += 1
    escolha = int(input('Digite um número de 1 a 10 e tente adivinhar: '))
    
    if escolha == aleatorio:
        print(f'Você acertou, foram {cont} Tentativas.')
        break
    else:
        cont +=1
        print('Você errou, tente novamente.')
        
    saida = str(input('Deseja sair? [S/N]: ')).lower()
    if saida == 's':
        break
print('Fim de jogo.')
