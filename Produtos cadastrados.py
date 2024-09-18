import sqlite3

# Estabelecer conexão com o banco de dados
conexao = sqlite3.connect("cadastros.db")

# Criar um cursor para executar comandos SQL
cursor = conexao.cursor()

cursor.execute("SELECT * FROM produtos;")

produ = cursor.fetchall()

for prods in produ:
    print(prods)

conexao.close()