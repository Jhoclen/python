


lista = {'brasil':'brasilia', 'argentina':'buenos aires','espanha':'barcelona'}

us = input('digite um país: ')

if us in lista:
    print(f'o país é {us} e sua capital é {lista[us]}') 
else:
    print('nome invalido')    

    