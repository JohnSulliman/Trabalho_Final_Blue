from funcoes import insert, select, update, delete

def insert_genero(nome):
    insert("generos", ["nome"], [nome])

def alterar_genero(id, nome):
    return update("generos", ["nome"], [id], [nome])

def get_genero(nome):
    return select("generos", "nome", nome)