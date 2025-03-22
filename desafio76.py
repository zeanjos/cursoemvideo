produto = ("Lápis", 1.50, "Borracha", 2.00, "Caneta", 3.00, "Caderno", 30.00, "Estojo", 25.90, "Marca Texto", 5.99)
print('-'*50)
for i in range(0, len(produto), 2):
    print(f"{produto[i]:.<30} {' R$ '}{produto[i + 1]}")
print("-"*50)