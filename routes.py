from flask import Flask, jsonify, request
from datetime import datetime, timedelta
from serializadores import *
from validacao import *
from models import *

app = Flask(__name__)

#--------------------------------------------Usuários-------------------------------------------------------------

@app.route("/usuarios", methods=["POST"])
def inserir_usuario():
    usuario = usuario_from_web(**request.json)
    if valida_usuario(**usuario):
        id_usuario = insert_usuario(**usuario)
        usuario_cadastrado = get_usuario(id_usuario)
        return jsonify(usuario_from_db(usuario_cadastrado))
    else:
        return jsonify({"Erro": "Usuário inválido!"})

@app.route("/usuarios/<int:id>", methods=["PUT", "PATCH"])
def alterar_usuario(id):
    usuario = usuario_from_web(**request.json)
    if valida_usuario(**usuario):
        update_usuario(id, **usuario)
        usuario_cadastrado = get_usuario(id)
        return jsonify(usuario_from_db(usuario_cadastrado))
    else:
        return jsonify({"Erro": "Usuário inválido!"})

@app.route("/usuarios", methods=["GET"])
def buscar_usuario():
    nome_completo = nome_usuario_from_web(**request.args)
    usuarios = select_usuarios(nome_completo)
    usuarios_from_db = [usuario_from_db(usuario) for usuario in usuarios]
    return jsonify(usuarios_from_db)

@app.route("/usuarios/<int:id>", methods=["DELETE"])
def apagar_usuario(id):
    try:
        delete_usuario(id)
        return jsonify("O usuário foi deletado!")#Para arquivos deletados, normalmente retornamos "return ("", 204)"
    except:
        return jsonify({"Erro": "Usuário não pode ser deletado ou não existe!"})

#---------------------------------------------Gêneros-------------------------------------------------------------

@app.route("/generos", methods=["POST"])
def inserir_genero():
    genero = genero_from_web(**request.json)
    if valida_genero(**genero):
        id_genero = insert_genero(**genero)
        genero_cadastrado = get_genero(id_genero)
        return jsonify(genero_from_db(genero_cadastrado))
    else:
        return jsonify({"Erro": "Gênero inválido!"})

@app.route("/generos/<int:id>", methods=["PUT", "PATCH"])
def alterar_genero(id):
    genero = genero_from_web(**request.json)
    if valida_genero(**genero):
        update_genero(id, **genero)
        genero_cadastrado = get_genero(id)
        return jsonify(genero_from_db(genero_cadastrado))
    else:
        return jsonify({"Erro": "Gênero inválido!"})

@app.route("/generos", methods=["GET"])
def buscar_genero():
    nome_completo = nome_genero_from_web(**request.args)
    generos = select_generos(nome_completo)
    generos_from_db = [genero_from_db(genero) for genero in generos]
    return jsonify(generos_from_db)

@app.route("/generos/<int:id>", methods=["DELETE"])
def apagar_genero(id):
    try:
        delete_genero(id)
        return jsonify("O Gênero foi deletado!")#Para arquivos deletados, normalmente retornamos "return ("", 204)"
    except:
        return jsonify({"Erro": "Gênero não pode ser deletado ou não existe!"})

#---------------------------------------------Diretores-----------------------------------------------------------

@app.route("/diretores", methods=["POST"])
def inserir_diretor():
    diretor = diretor_from_web(**request.json)
    if valida_diretor(**diretor):
        id_diretor = insert_diretor(**diretor)
        diretor_cadastrado = get_diretor(id_diretor)
        return jsonify(diretor_from_db(diretor_cadastrado))
    else:
        return jsonify({"Erro": "Diretor inválido!"})

@app.route("/diretores/<int:id>", methods=["PUT", "PATCH"])
def alterar_diretor(id):
    diretor = diretor_from_web(**request.json)
    if valida_diretor(**diretor):
        update_diretor(id, **diretor)
        diretor_cadastrado = get_diretor(id)
        return jsonify(diretor_from_db(diretor_cadastrado))
    else:
        return jsonify({"Erro": "Diretor inválido!"})

@app.route("/diretores", methods=["GET"])
def buscar_diretor():
    nome_completo = nome_diretor_from_web(**request.args)
    diretores = select_diretores(nome_completo)
    diretores_from_db = [diretor_from_db(diretor) for diretor in diretores]
    return jsonify(diretores_from_db)

@app.route("/diretores/<int:id>", methods=["DELETE"])
def apagar_diretor(id):
    try:
        delete_diretor(id)
        return jsonify("O diretor foi deletado!")#Para arquivos deletados, normalmente retornamos "return ("", 204)"
    except:
        return jsonify({"Erro": "Diretor não pode ser deletado ou não existe!"})

#------------------------------------------------Filmes-----------------------------------------------------------

@app.route("/filmes", methods=["POST"])
def inserir_filme():
    filme = diretor_from_web(**request.json) and genero_from_web(**request.json) and filme_from_web(**request.json)
    if valida_filme(**filme) and valida_diretor(**filme) and valida_genero(**filme):
        id_filme = insert_filme(**filme)
        filme_cadastrado = get_filme(id_filme)
        return jsonify(filme_from_db(filme_cadastrado))
    else:
        return jsonify({"Erro": "Filme inválido!"})

@app.route("/filmes/<int:id>", methods=["PUT", "PATCH"])
def alterar_filmes(id):
    filme = diretor_from_web(**request.json) and genero_from_web(**request.json) and filme_from_web(**request.json)
    if valida_filme(**filme) and valida_diretor(**filme) and valida_genero(**filme):
        update_filme(id, **filme)
        filme_cadastrado = get_filme(id)
        return jsonify(filme_from_db(filme_cadastrado))
    else:
        return jsonify({"Erro": "Filme inválido!"})

@app.route("/filmes", methods=["GET"])
def buscar_filmes():
    nome_filme = nome_filme_from_web(**request.args)
    filmes = select_filmes(nome_filme)
    filmes_from_db = [filme_from_db(filme) for filme in filmes]
    return jsonify(filmes_from_db)

@app.route("/filmes/<int:id>", methods=["DELETE"])
def apagar_filme(id):
    try:
        delete_filme(id)
        return jsonify("O filme foi deletado!")#Para arquivos deletados, normalmente retornamos "return ("", 204)"
    except:
        return jsonify({"Erro": "Filme não pode ser deletado ou não existe!"})

#----------------------------------------Locações e Pagamentos----------------------------------------------------

@app.route("/locacoes", methods=["POST"])
def inserir_locacao():
    locacao = filme_from_web(**request.json) and usuario_from_web(**request.json) and locacao_from_web(**request.json)
    if valida_locacao(**locacao):
        datetime.now()
        inicio = datetime.now()
        fim = inicio + timedelta(hours=48, minutes=0, seconds=0)
        id_locacao = insert_locacao(inicio, fim, **locacao)
        locacao_cadastrada = get_locacao(id_locacao)
        return jsonify(locacao_from_db(locacao_cadastrada))
    else:
        return jsonify({"Erro": "Locação inválida!"})

# @app.route("/filmes/<int:id>", methods=["PUT", "PATCH"])
# def alterar_filmes(id):
#     filme = diretor_from_web(**request.json) and genero_from_web(**request.json) and filme_from_web(**request.json)
#     if valida_filme(**filme) and valida_diretor(**filme) and valida_genero(**filme):
#         update_filme(id, **filme)
#         filme_cadastrado = get_filme(id)
#         return jsonify(filme_from_db(filme_cadastrado))
#     else:
#         return jsonify({"Erro": "Filme inválido!"})
#
# @app.route("/filmes", methods=["GET"])
# def buscar_filmes():
#     nome_filme = nome_filme_from_web(**request.args)
#     filmes = select_filmes(nome_filme)
#     filmes_from_db = [filme_from_db(filme) for filme in filmes]
#     return jsonify(filmes_from_db)
#
# @app.route("/filmes/<int:id>", methods=["DELETE"])
# def apagar_filme(id):
#     try:
#         delete_filme(id)
#         return jsonify("O filme foi deletado!")#Para arquivos deletados, normalmente retornamos "return ("", 204)"
#     except:
#         return jsonify({"Erro": "Filme não pode ser deletado ou não existe!"})




# Fazer uma locação => enviar id_filme, id_usuario, tipo_pagamento, data_inicio
#  Criar um pagamento, junto com a locação
#  Colocar a data de fim 48h depois da data de inicio (automático)
#  Preencher o valor do pagamento com o valor do filme
#  Gerar um código de pagamento aleatório pra preencher no código de pagamento
#  Colocar o status aleatório
# Checar uma locação: Listar locações pelo id do usuário
# Exibir locação pelo id
# Listar locações por id do filme
#  Locaçõed devem ter, nome do usuário, nome do filme, data da locação, status do pagamento

# Como adicionar 48h numa data
# from datetime import datetime, timedelta
# datetime.now()
# datetime.datetime(2021, 4, 30, 22, 37, 4, 387981)
# agora = datetime.now()
# agora + timedelta(hours=48)
# datetime.datetime(2021, 5, 2, 22, 37, 8, 762753)


# import random
#
# mylist = ["apple", "banana", "cherry"]
#
# print(random.choice(mylist))

if __name__ == "__main__":
    app.run()