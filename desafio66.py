cont = n = s = 0
while n != 999:
    n = int(input('Digite um número:'))
    if n == 999:
        break
    cont += 1
    s += n
print(f'Foram digitados {cont} Números, a soma entre os números é de {s}.')
