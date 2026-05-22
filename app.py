from banco import conectar, criar_tabelas
from flask import Flask, render_template, request

from diagnostico import (
    analisar_sistema,
    explicar_resultado
)

app = Flask(__name__)
criar_tabelas()


@app.route("/", methods=["GET", "POST"])
def index():

    resultado = None
    explicacao = None

    if request.method == "POST":

        lentidao = request.form["lentidao"]
        temperatura = int(request.form["temperatura"])
        ram = int(request.form["ram"])
        travamentos = request.form["travamentos"]

        resultado = analisar_sistema(
            lentidao,
            temperatura,
            ram,
            travamentos
        )

        explicacao = explicar_resultado(resultado)

    return render_template(
        "index.html",
        resultado=resultado,
        explicacao=explicacao
    )

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():

    if request.method == "POST":

        nome = request.form["nome"]
        email = request.form["email"]
        senha = request.form["senha"]

        conexao = conectar()

        cursor = conexao.cursor()

        cursor.execute(
            """
            INSERT INTO usuarios
            (nome, email, senha)

            VALUES (?, ?, ?)
            """,
            (nome, email, senha)
        )

        conexao.commit()

        conexao.close()

        return "Usuário cadastrado com sucesso!"

    return render_template("cadastro.html")

if __name__ == "__main__":
    app.run(debug=True)