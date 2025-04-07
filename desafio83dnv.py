expressao = str(input('Digite sua expressão: '))
pilha = []
for simbolo in expressao:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha > 0):
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('A sua expressão está correta!')
else:
    print('A sua expressão está invalida!')