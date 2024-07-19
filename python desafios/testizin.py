


def soma(*numeros):
    r = 0
    for num in numeros:
        r += num
    return r    

x = soma(1,2,3,4,5,6)
print(x)