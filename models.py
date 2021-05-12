from funcoes import query, insert, select, select_like, update, delete

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

def update_genero(id_genero, nome):
    update("generos", "id", id_genero, ["nome"], [nome])

def get_genero(id_genero):
    return select("generos", "id", id_genero)[0]

def select_generos(nome):
    return select_like("generos", "nome", nome)

def delete_genero(id_genero):
    delete("generos", "id", id_genero)

#---------------------------------------------Diretores-----------------------------------------------------------

def insert_diretor(nome_completo):
    return insert("diretores", ["nome_completo"], [nome_completo])

def update_diretor(id_diretor, nome_completo):
    update("diretores", "id", id_diretor, ["nome_completo"], [nome_completo])

def get_diretor(id_diretor):
    return select("diretores", "id", id_diretor)[0]

def select_diretores(nome_completo):
    return select_like("diretores", "nome_completo", nome_completo)

def delete_diretor(id_diretor):
    delete("diretores", "id", id_diretor)

#------------------------------------------------Filmes-----------------------------------------------------------

def insert_filme(titulo, ano, classificacao, preco, diretores_id, generos_id):
    return insert("filmes", ["titulo", "ano", "classificacao", "preco", "diretores_id", "generos_id"],
                  [titulo, ano, classificacao, preco, diretores_id, generos_id])

def update_filme(id_filme, titulo, ano, classificacao, preco, diretores_id, generos_id):
    update("filmes", "id", id_filme, ["titulo", "ano", "classificacao", "preco", "diretores_id", "generos_id"],
           [titulo, ano, classificacao, preco, diretores_id, generos_id])

def get_filme(self):
    return query(f"""SELECT 
                 *
                 FROM filmes
                 INNER JOIN diretores on filmes.diretores_id = diretores.id
                 INNER JOIN generos on filmes.generos_id = generos.id""")[0]

def select_filmes(id_filme):
    return select_like("filmes", "id", id_filme)

def delete_filme(id_filme):
    delete("filmes", "id", id_filme)

#----------------------------------------Locações e Pagamentos----------------------------------------------------

def insert_locacao(data_inicio, data_fim, filmes_id, usuarios_id):
    return insert("locacoes", ["data_inicio", "data_fim", "filmes_id", "usuarios_id"],
                  [data_inicio, data_fim, filmes_id, usuarios_id])

def update_locacao(id, data_inicio, data_fim, filmes_id, usuarios_id):
    update("locacao", "id", id, ["data_inicio", "data_fim", "filmes_id", "usuarios_id"],
           [data_inicio, data_fim, filmes_id, usuarios_id])

def get_locacao(self):
    return query(f"""SELECT 
                 *
                 FROM locacoes
                 INNER JOIN filmes on locacoes.filmes_id = filmes.id
                 INNER JOIN usuarios on locacoes.usuarios_id = usuarios.id""")[0]
#
# def select_filmes(id_filme):
#     return select_like("filmes", "id", id_filme)
#
# def delete_filme(id_filme):
#     delete("filmes", "id", id_filme)

def insert_pagamento(status, codigo_pagamento, data, locacoes_id, *valor, **tipo):
    return insert("pagamentos", ["tipo", "status", "codigo_pagamento", "valor", "data", "locacoes_id"],
                  [tipo, status, codigo_pagamento, valor, data, locacoes_id])


def get_pagamento(id):
    return select("pagamentos", "id", id)