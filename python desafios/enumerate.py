


lista = ['maça', 'batata', 'goiaba', 'abacaxi']


def index(lista1, item):
    for i, valor in enumerate(lista1):
        if valor == item:
            return i
    return -1


print(index(lista, 'goiaba'))

for e, valores in enumerate(lista):
    if valores == 'abacaxi':
        print(e)

for itens in enumerate(lista):
    print(itens)