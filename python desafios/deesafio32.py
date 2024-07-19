


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista = []
fun = lambda num: num ** 2

for lem in numeros:
    lista.append(fun(lem))

print(numeros)
print(lista)  