import psycopg2
db = "crud"
user = "postgres"
senha = "root"

conn = psycopg2.connect(
    dbname= db,
    user= user,
    password= senha,
    host="localhost",
    port="5432"
)
conn.autocommit = True
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    curso VARCHAR(100) NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS notas (
    id SERIAL PRIMARY KEY,
    aluno_id INTEGER REFERENCES alunos(id) ON DELETE CASCADE,
    nota NUMERIC(4,2) NOT NULL
);
""")


def inserir_aluno(nome, curso):
    conn = psycopg2.connect(
    dbname= db,
    user= user,
    password= senha,
    host="localhost",
    port="5432"
)
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute("INSERT INTO alunos (nome, curso) VALUES (%s, %s)", (nome, curso))
    cursor.close()
    conn.close()

def inserir_nota(aluno_id, nota):
    conn = psycopg2.connect(
    dbname= db,
    user= user,
    password= senha,
    host="localhost",
    port="5432"
)
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute("INSERT INTO notas (aluno_id, nota) VALUES (%s, %s)", (aluno_id, nota))
    cursor.close()
    conn.close()

def listar_alunos():
    conn = psycopg2.connect(
    dbname= db,
    user= user,
    password= senha,
    host="localhost",
    port="5432"
)
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM alunos")
    for aluno in cursor.fetchall():
        print(aluno)    
    cursor.close()
    conn.close()

def listar_notas():

    conn = psycopg2.connect(
    dbname= db,
    user= user,
    password= senha,
    host="localhost",
    port="5432"
)
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute("""
        SELECT n.id, a.nome, n.nota
        FROM notas n
        JOIN alunos a ON a.id = n.aluno_id
    """)
    for nota in cursor.fetchall():
        print(nota)  

    cursor.close()
    conn.close()


def atualizar_nota(nota_id, nova_nota):

    conn = psycopg2.connect(
    dbname= db,
    user= user,
    password= senha,
    host="localhost",
    port="5432"
)
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute("UPDATE notas SET nota = %s WHERE id = %s", (nova_nota, nota_id))    
    cursor.close()
    conn.close()

def deletar_aluno(aluno_id):

    conn = psycopg2.connect(
    dbname= db,
    user= user,
    password= senha,
    host="localhost",
    port="5432"
)
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute("DELETE FROM alunos WHERE id = %s", (aluno_id,))
    cursor.close()
    conn.close()


def buscar_aluno_por_id(id_aluno):
    conn = psycopg2.connect(
        dbname= db,
        user= user,
        password= senha,
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()

    cursor.execute("""
        SELECT alunos.id, alunos.nome, alunos.curso, notas.nota
        FROM alunos
        LEFT JOIN notas ON alunos.id = notas.aluno_id
        WHERE alunos.id = %s
    """, (id_aluno,))

    resultados = cursor.fetchall()

    cursor.close()
    conn.close()

    if not resultados:
        return []
   
    dados = []
    for id, nome, curso, nota in resultados:
        dados.append([id, nome, curso, nota])

    return dados


cursor.close()
conn.close()
