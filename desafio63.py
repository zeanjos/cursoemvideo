
num_fim = int(input('Digite o número final: '))
anterior = 0
atual = 1
print(anterior)
while atual < num_fim:
    print(f'A sequência de fibonnaci é: {atual}')
    novo = anterior + atual
    anterior = atual
    atual = novo
    
        
