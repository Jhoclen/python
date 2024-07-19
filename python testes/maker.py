

'''valor = int(input('qual o valor do produto: '))

while valor > 20:
    valor = valor * 1.1
    print(f'o valor total do seu produto será R$ {valor}')
    break'''


#calcular o fatorial
'''numero = int(input('qual o número queee você quer caulcular o fatorical:'))
num = numero


def fa(numero):
    resultado = 1
    while numero > 1:
        resultado *= numero
        numero -= 1
    return resultado    

x = fa(numero)
print(f' o fatorial de {num} = {x}')'''




'''numeros = [x * 10 for x in range(1, 10)] 

print(numeros)'''

# conhecimento de class
from datetime import datetime
class Funcionario:

    def __init__(self, nome, CPF, ano_nascimento):
        self.nome = nome
        self.CPF = CPF
        self.ano_nascimento = ano_nascimento

    def nome_cpf(self):
        return f'{self.nome} {self.CPF}'    

    def idade_funcionario(self):
        ano_atual = datetime.now().year
        self.ano_nascimento = int(ano_atual - self.ano_nascimento)
        return self.ano_nascimento
        

n1 = Funcionario('jao', '123', 2002)
n2 = Funcionario('rafa', '321', 2004)
n3 = Funcionario('deba', '452', 1999)

print(n1.nome)
print(n2.nome)
print(n3.nome)
print(Funcionario.nome_cpf(n2))
print(Funcionario.idade_funcionario(n2))
