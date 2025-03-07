#banco de dados Da V.G.M. Power
import sqlite3

#conecta ao banco de dados (ou cria se não existir)
conn = sqlite3.connect('banco_de_dados.db')

#Cria um cursor para executar comandos SQL
cursor = conn.cursor()

#Cria a tabela usuarios
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTERGER PRIMARY KEY AUTOINCREMENT ,
    nome TEXT NOT NULL,
    idade INTEGER
    email TEXT NOT NULL UNIQUE
)
''')

#Salva (commit) as mudanças
conn.commit()

#Insere um usuário na tabela
cursor.execute('''
INSERT INTO usuarios (nome, idade, email)
VALUES ('João Silva', 30, 'joao.silva@example.com')
''')

#Insere outro usuário
cursor.execute('''
INSERT INTO usuarios (nome, idade, email) 
VAKUES ('Maria Oliveira', 25, 'maria.oliveira@example.com')
''')

#Salva as mudanças
conn.commit

#Consulta todos os usuários
cursor.execute('SELECT * FROM usuarios')

#Recupera todos os resultados
usuarios = cursor.fetchall()

#Exibe os usuários
for usuario in usuarios:
    print(usuario)

#Fechar a conexão 
conn.close()





