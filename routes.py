from flask import Flask, jsonify, request
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
    filme = filme_from_web(**request.json)
    if valida_filme(**filme):
        id_filme = insert_filme(**filme)
        filme_cadastrado = get_filme(id_filme)
        return jsonify(filme_from_db(filme_cadastrado))
    else:
        return jsonify({"Erro": "Filme inválido!"})
#
# @app.route("/diretores/<int:id>", methods=["PUT", "PATCH"])
# def alterar_diretor(id):
#     diretor = diretor_from_web(**request.json)
#     if valida_diretor(**diretor):
#         update_diretor(id, **diretor)
#         diretor_cadastrado = get_diretor(id)
#         return jsonify(diretor_from_db(diretor_cadastrado))
#     else:
#         return jsonify({"Erro": "Diretor inválido!"})
#
# @app.route("/diretores", methods=["GET"])
# def buscar_diretor():
#     nome_completo = nome_diretor_from_web(**request.args)
#     diretores = select_diretores(nome_completo)
#     diretores_from_db = [diretor_from_db(diretor) for diretor in diretores]
#     return jsonify(diretores_from_db)
#
# @app.route("/diretores/<int:id>", methods=["DELETE"])
# def apagar_diretor(id):
#     try:
#         delete_diretor(id)
#         return jsonify("O diretor foi deletado!")#Para arquivos deletados, normalmente retornamos "return ("", 204)"
#     except:
#         return jsonify({"Erro": "Diretor não pode ser deletado ou não existe!"})


if __name__ == "__main__":
    app.run()