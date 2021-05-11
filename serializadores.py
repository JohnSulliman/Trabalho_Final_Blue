from datetime import datetime, timedelta

#--------------------------------------------Usuários-------------------------------------------------------------

def usuario_from_web(**kwargs):
    return {
        "nome_completo": kwargs["nome_completo"] if "nome_completo" in kwargs else "",
        "CPF": kwargs["CPF"] if "CPF" in kwargs else "",
    }

def usuario_from_db(usuario):
    return {
        "id": usuario["id"],
        "nome_completo": usuario["nome_completo"],
        "CPF": usuario["CPF"],
    }

def nome_usuario_from_web(**kwargs):
    return kwargs["nome_completo"] if "nome_completo" in kwargs else ""



#---------------------------------------------Gêneros-------------------------------------------------------------

def genero_from_web(**kwargs):
    return {
        "nome": kwargs["nome"] if "nome" in kwargs else "",
    }

def genero_from_db(genero):
    return {
        "id": genero["id"],
        "nome": genero["nome"],
    }

def nome_genero_from_web(**kwargs):
    return kwargs["nome"] if "nome" in kwargs else ""

#---------------------------------------------Diretores-----------------------------------------------------------

def diretor_from_web(**kwargs):
    return {
        "nome_completo": kwargs["nome_completo"] if "nome_completo" in kwargs else "",
    }

def diretor_from_db(diretor):
    return {
        "id": diretor["id"],
        "nome_completo": diretor["nome_completo"],
    }

def nome_diretor_from_web(**kwargs):
    return kwargs["nome_completo"] if "nome_completo" in kwargs else ""

#------------------------------------------------Filmes-----------------------------------------------------------

def filme_from_web(**kwargs):
    return {
        "titulo": kwargs["titulo"] if "titulo" in kwargs else "",
        "ano": kwargs["ano"] if "ano" in kwargs else "",
        "classificacao": kwargs["classificacao"] if "classificacao" in kwargs else "",
        "preco": kwargs["preco"] if "preco" in kwargs else "",
        "diretores_id": kwargs["diretores_id"] if "diretores_id" in kwargs else "",
        "generos_id": kwargs["generos_id"] if "generos_id" in kwargs else "",
    }

def filme_from_db(filme):
    return {
        "id": filme["id"],
        "titulo": filme["titulo"],
        "ano": filme["ano"],
        "classificacao": filme["classificacao"],
        "preco": str(filme["preco"]),
        "diretores_id": filme["diretores_id"],
        "generos_id": filme["generos_id"],

    }

def nome_filme_from_web(**kwargs):
    return kwargs["titulo"] if "titulo" in kwargs else ""

#----------------------------------------Locações e Pagamentos----------------------------------------------------

def locacao_from_web(**kwargs):
    return {
        "filmes_id": kwargs["filmes_id"] if "filmes_id" in kwargs else "",
        "usuarios_id": kwargs["usuarios_id"] if "usuarios_id" in kwargs else "",
    }

def locacao_from_db(locacao):
    return {
        "id": locacao["id"],
        "data_inicio": datetime.now(),
        "data_fim": timedelta(hours=48, minutes=0, seconds=0),
        "filmes_id": locacao["filmes_id"],
        "usuarios_id": locacao["usuarios_id"],
    }

def id_locacao_from_web(**kwargs):
    return kwargs["id"] if "id" in kwargs else ""