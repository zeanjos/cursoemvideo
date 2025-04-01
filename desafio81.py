numeros = []
continua = True

while continua:
    num = int(input('Digite um número ou digite -1 se desejar parar:'))
    if num == -1:
        print('Voce desejou parar.')
        continua = False
    else:
        numeros.append(num)
        quantia_cinco = numeros.count(5)
        
print(
    f'Foram digitados: {len(numeros)} Numerações, os números em ordem decrescente: {sorted(numeros, reverse=True)}', 
    f'O número cinco aparece {quantia_cinco}, {"Vezes" if quantia_cinco > 1 else 'vez'}' 
    if quantia_cinco > 0 else 'O número cinco não aparece na lista'
)