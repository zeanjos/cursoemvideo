estado = {}
brasil = []
for c in range(0,3):
    estado['uf'] = str(input('Unidade federativa: ')).strip().capitalize()
    estado['sigla'] = str(input('Sigla do estado: ')).strip().upper()
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')