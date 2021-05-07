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
        return jsonify({"erro": "Usuário inválido!"})

@app.route("/usuarios/<int:id>", methods=["PUT", "PATCH"])
def alterar_usuario(id):
    usuario = usuario_from_web(**request.json)
    if valida_usuario(**usuario):
        update_usuario(id, **usuario)
        usuario_cadastrado = get_usuario(id)
        return jsonify(usuario_from_db(usuario_cadastrado))
    else:
        return jsonify({"erro": "Usuário inválido!"})

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
        return jsonify("O usuário foi deletado!")
    except:
        return jsonify({"erro": "Usuário não pode ser deletado ou não existe!"})

#---------------------------------------------Gêneros-------------------------------------------------------------

@app.route("/generos", methods=["POST"])
def inserir_genero():
    genero = genero_from_web(**request.json)
    if valida_genero(**genero):
        insert_genero(**genero)
        genero_criado = get_genero(genero["nome"])
        return jsonify(genero_from_db(genero_criado))
    else:
        return jsonify({"erro": "gênero inválido"})

@app.route("/generos/<int:id>", methods=["PUT"])
def alterar_genero(id):
    novo_genero = genero_from_web(**request.json)
    if valida_genero(**novo_genero):
        update_genero(id, **novo_genero)
        genero_atualizado = get_genero(novo_genero["nome"])
        return jsonify(genero_from_db(genero_atualizado))
    else:
        return jsonify({"erro": "não foi possível atualizar o item gênero"})

@app.route("/generos", methods=["GET"])
def buscar_genero():
    nome_genero = nome_genero_from_web(**request.args)
    generos = select_genero(nome_genero)
    generos_from_db = [genero_from_db(genero) for genero in generos]
    return jsonify(generos_from_db)

@app.route("/generos/<int:id>", methods=["DELETE"])
def apagar_genero(id):
    try:
        delete_genero(id)
        return jsonify("O gênero foi deletado!")
    except:
        return jsonify({"erro": "Gênero não pode ser deletado ou não existe!"})

#---------------------------------------------Diretores-----------------------------------------------------------


if __name__ == "__main__":
    app.run()