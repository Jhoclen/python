

def fat (n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fat(n-1)  
'''def fat(numero):
    x = 1
    res = 1
    while x <= numero:
        res *= x
        x +=1
    return res'''

num = int(input('qual numero vc quer calcular o fatorial: '))

print(f'o fatorial de {num} é {fat(num)}')