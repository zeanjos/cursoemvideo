lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')

#for cont in range(0, len(lanche)):
#    print(f'Eu vou comer {lanche[cont]} na posição {cont}')




# Tuplas são imutaveis!
# Este comando está errado pois tuplas são imutaveis, aqui está tentando fazer a atribuição de outra string lanche[1] = 'Refrigerante'
for pos, comida in enumerate(lanche):
   print(f'Eu vou comer {comida} na posição {pos}')
#print('É o bulking não tem jeito')