from flask import Flask, jsonify, request
from serializadores import *
from validacao import *
from models import *

app = Flask(__name__)

@app.route("/generos", methods=["POST"])
def inserir_genero():
    genero = genero_from_web(**request.json)
    if valida_genero(**genero):
        insert_genero(**genero)
        genero_criado = get_genero(genero["nome"])
        return jsonify(genero_from_db(genero_criado))
    else:
        return jsonify({"erro": "gênero inválido"})

@app.route("/generos/<int:id>", methods=["PATCH"])
def update_genero(id):
    novo_genero = genero_from_web(**request.json)
    if valida_genero(**novo_genero):
        alterar_genero(id, **novo_genero)
        genero_atualizado = get_genero(novo_genero["nome"])
        return jsonify(genero_from_db(genero_atualizado))
    else:
        return jsonify({"erro": "não foi possível atualizar o item gênero"})

if __name__ == "__main__":
    app.run()