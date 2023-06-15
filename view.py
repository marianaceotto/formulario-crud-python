import sqlite3 as lite

#CRUD
#C = Creaty
#R = Ready 
#U = Update 
#D - Delete 

conexao = lite.connect('dados.db')

# cadastrar usuário
def inserir_info(i):
    with conexao:
        cur = conexao.cursor()
        query = "INSERT INTO formulario (nome, email, telefone, dia_em, estado, comentario) VALUES (?,?,?,?,?,?)"
        cur.execute(query, i)   
 
# acessar infos
def mostar_info():
    lista = []
    with conexao:
        cur = conexao.cursor()
        query = "SELECT * FROM formulario"
        cur.execute(query)    
        info = cur.fetchall()
        
        for i in info: 
            lista.append(i)
    return lista
            
 

      
# atualizar info  
def atualizar_info(i):
    with conexao:
        cur = conexao.cursor()
        query = "UPDATE formulario SET nome=?, email=?, telefone=?, dia_em=?, estado=?, comentario=? WHERE id=?"
        cur.execute(query, i)



# deletar info
def deletar_info(i):
    with conexao:
        cur = conexao.cursor()
        query = "DELETE FROM formulario WHERE id=?"
        cur.execute(query, i)
