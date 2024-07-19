


'''antes - cozinhar por mais aluns minutos
48 - selada
54 - Ao ponto para mal
60 - ao ponto
65 - ao ponto para bem
71 - bem passada'''
try:
    graus = int(input('Qual a temperatura da carne ? '))
except ValueError:
    print('digite um valor valido')    

try:
    if graus < 48:
        print('cozinhar por mais alguns minutos')
    elif graus in range(48, 54):
        print('selada')
    elif graus in range(54, 60):
        print('Ao ponto para mal')
    elif graus in range(60, 65):
        print('ao ponto')
    elif graus in range(65, 71):
        print('ao ponto para bem')
    elif graus >= 71:
        print('bem passada')    
except NameError:
    pass
    
'''if graus < 48:
    print('cozinhar por mais alguns minutos')
elif 48 <= graus < 54:
    print('selada')
elif 54 <= graus < 60:
    print('Ao ponto para mal')
elif 60 <= graus < 65:
    print('ao ponto')
elif 65 <= graus < 71:
    print('ao ponto para bem')
elif graus >= 71:
    print('bem passada') '''   