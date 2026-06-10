from flask import Flask, render_template, request

from diagnostico import (
    analisar_sistema,
    explicar_resultado
)

from banco import (
    criar_tabelas,
    salvar_diagnostico,
    listar_historico,
    obter_estatisticas,
    gerar_grafico_diagnosticos
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

        salvar_diagnostico(
            temperatura,
            ram,
            travamentos,
            resultado,
            explicacao
        )

    return render_template(
        "index.html",
        resultado=resultado,
        explicacao=explicacao
    )

@app.route("/historico")
def historico():

    dados = listar_historico()

    return render_template(
        "historico.html",
        dados=dados
    )
@app.route("/dashboard")
def dashboard():

    gerar_grafico_diagnosticos()

    estatisticas = obter_estatisticas()

    return render_template(
        "dashboard.html",
        estatisticas=estatisticas
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

