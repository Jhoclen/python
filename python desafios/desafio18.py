


lista = ['gol','fusca','jeep']

carro = input('insira o nome do carro que deseja comprar: ')
carro = carro.lower()

if carro in lista:
    print(' carro em estoque')
else:
    print('este carro não está em estoque')    