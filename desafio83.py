conta_aberto = conta_fechado = 0
num = str(input('Digite sua expressão: '))
conta_aberto = num.count('(')
conta_fechado = num.count(')')
if conta_aberto == conta_fechado:
    print('Sua expressão está CORRETA!')
else:
    print('Sua expressão está errada!')