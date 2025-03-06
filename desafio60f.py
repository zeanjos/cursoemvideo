n = int(input('Digite o número que deseja fatorar: '))
c = n
s = 0
while c > 0:
    c -= 1
    s = n * c
s *= c
print(f'{n} x {c} = {s}')

