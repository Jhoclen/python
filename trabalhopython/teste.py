import psycopg2
import tabelas 

valor = []
chave = ['id', 'nome', 'curso' ,'nota']
valor = tabelas.buscar_aluno_por_id(3)

print(valor)
for a in valor:
    print(a)
