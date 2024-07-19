




funcionarios = ['ana', 'marcos', 'alice', 'pedro', 'sophia', 'bruno', 'melissa']
turno_dia = ['ana', 'marcos', 'alice', 'melissa']
turno_noite = ['pedro', 'sophia', 'bruno']
tem_carro = ['marcos', 'alice', 'bruno', 'melissa']

lista1 = set(tem_carro).intersection(turno_noite)
print(lista1)

lista2 = set(tem_carro).intersection(turno_dia)
print(lista2)

lista3 = set(funcionarios).difference(tem_carro)
print(lista3)
'''num1 = set(funcionarios)
num2 = set(turno_dia)
num3 = set(turno_noite)
num4 = set(tem_carro)

print(num4 & num3)
print(num4 & num2)
print(num1 - num4)'''