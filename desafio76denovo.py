lista = ('Lapis', 1.50,
          'Borracha', 3,
            'Caneta', 2,
              'Caderno', 30,
                'Mochila', 100,
                'Estojo', 25)
for i in range(0, len(lista), 2):
    print(f'{lista[i]:.<20} {'R$ '}{lista[i+1]:.2f}')