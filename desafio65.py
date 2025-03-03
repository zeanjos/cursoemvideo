num = 0
menor = 0
maior = 0
soma = 0
media = 0
desejo = str('s').lower()
while desejo == 's':
    num = int(input('Digite o número desejado: '))
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    desejo = str(input('Deseja continuar [S] ou [N]: ')).lower()
        