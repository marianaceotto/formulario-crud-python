# criando conexao

import sqlite3 as lite

conexao = lite.connect('dados.db')

# criando tabela

with conexao:
    cur = conexao.cursor()
    cur.execute("CREATE TABLE formulario(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT, telefone TEXT, dia_em DATE, estado TEXT, comentario TEXT)")


# with conexao:
#     cur = conexao.cursor()
#     cur.execute("DROP TABLE formulario")

