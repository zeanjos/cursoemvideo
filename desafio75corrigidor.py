
num = tuple(int(input('Digite um número: ')) for c in range(4))
print(f'Os números digitados foram: {num}')
if 3 in num:
    print(f'O número 3 foi digitado na posição:  {num.index(3) + 1}')
if 9 in num:
    print(f'O número 9 foi digitado {num.count(9)} Vezes')
for n in num:
    if n % 2 == 0:
        print(n, end= '')
print(f'Os valores pares digitados são: {n}')
    
