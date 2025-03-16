c = s = n = 0
while True:
    n = int(input('Digite um valor [999 Para parar]: '))
    if n == 999:
        break
    c += 1
    s += n
if c  == 1:
    print(f'Foram digitados apenas {c} Número, não existe soma pois só foi digitado {c}')
else:
    print(f'Foram digitados {c} Número, A soma entre os números é {s} ')