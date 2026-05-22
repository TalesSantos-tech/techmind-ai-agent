from flask import Flask, render_template, request

from diagnostico import (
    analisar_sistema,
    explicar_resultado
)

app = Flask(__name__)


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


if __name__ == "__main__":
    app.run(debug=True)