
# map função

'''lista = [1, 2, 2, 4]

def mul(x):
    return x * 2

list1 = map(mul, lista)

lista.append(30)
print(list(list1))'''

# List Comprehension
numeros = [x * 10 for x in range(5)]
print(numeros)

num = []
for y in range(5):
    num.append(y*10)
print(num)

lista = ['ruan', 'rafa', 'jhoclen', 'isabela']
valor = [itens for itens in lista if 'r' in itens]
print(valor, 'valor xxxxxxxxxxxxxxxxxxxxxx')

valor1 = []

for iten in lista:
    if 'j' in iten:
        valor1.append(iten)

print(valor1)
