from funcoes import insert, select, select_like, update, delete

#--------------------------------------------Usuários-------------------------------------------------------------

def insert_usuario(nome_completo, CPF):
    return insert("usuarios", ["nome_completo", "CPF"], [nome_completo, CPF])

def update_usuario(id_usuario, nome_completo, CPF):
    update("usuarios", "id", id_usuario, ["nome_completo", "CPF"], [nome_completo, CPF])

def get_usuario(id_usuario):
    return select("usuarios", "id", id_usuario)[0]

def select_usuarios(nome_completo):
    return select_like("usuarios", "nome_completo", nome_completo)

def delete_usuario(id_usuario):
    delete("usuarios", "id", id_usuario)

#---------------------------------------------Gêneros-------------------------------------------------------------

def insert_genero(nome):
    return insert("generos", ["nome"], [nome])

def update_genero(id, nome):
    update("generos", "nome", nome, ["id"], [id])

def get_genero(nome):
    return select("generos", "nome", nome)

def select_genero(nome_genero):
    return select_like("generos", "id", nome_genero)

def delete_genero(id_genero):
    delete("generos", "id", id_genero)

#---------------------------------------------Diretores-----------------------------------------------------------

