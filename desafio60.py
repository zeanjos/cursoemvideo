mult = 1
um = 1
num = int(input('Digite um número: '))

while num > um:
    for i in range(num, 0, -1):
        mult *= i
        print(f'O resultado da fatoração deste número é: {mult}')
    break