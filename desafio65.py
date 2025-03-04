
num = 0
med = 0
menor = None
maior = None
soma = 0
media = 0
desejo = str('s').lower()
cont = 0
while desejo == 's':
    maior = num
    menor = num
    num = int(input('Digite o número desejado: '))
    cont += 1
    soma += num
    media = (soma / cont)
    if num > maior:
        maior = num
        
    if num > menor:
        menor = num
        
                
    if desejo == 's':
        desejo = str(input('Deseja continuar [S] ou [N]: ')).lower()
        print('Você escolheu continuar, prossiga.') 
       
    else:
        print(f'''A soma dos números digitados é {soma}\n
A média dos números digitados é: {media}''')
        print('Você escolheu sair, até mais!')
    
        