


def potencia(base,exp = 2):
    return base ** exp    
base = input('qual a base: ')
exp = input('qual o expoente: ')


try:
    if exp:
        print(f'o resultado: {potencia(int(base),int(exp))}')
    else:
        print(f'o resultado: {potencia(int(base))}')    
except ValueError:
    print('')
    print('Digite um número inteiro') 