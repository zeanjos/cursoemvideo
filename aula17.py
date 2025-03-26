num = []
cont = 0
while cont < 3:
    num.append(int(input('Digite um número: ')))
    cont += 1

for c, v in enumerate(num):
    print(f'Na posição {c}, encontrei o valor {v}')