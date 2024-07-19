



# redimento da lata
'''altura da parede 
largura da parede'''

rend = int(input(' qual o redimento da lata:'))
altura = int(input(' qual a altura da parede:'))
largura = int(input(' qual a largura da parede:'))


def xlata():
    area = (altura*largura) / rend
    print(f'voce precisa de {area} latas de tinta')

xlata()

