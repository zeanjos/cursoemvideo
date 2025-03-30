lista = []
continua = True
while continua:
    num = int(input('Digite um número ou 0 para sair: '))
    if num == 0:
        continua = False
    else:
        lista.append(num)
        menor = min(lista)
        maior = max(lista)
        indice_menor = lista.index(menor)
        indice_maior = lista.index(maior)
print(f'O menor valor digitado foi {menor} no indice {indice_menor} e o maior {maior} no indice {indice_maior}')