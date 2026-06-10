from datetime import datetime
import sqlite3

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt

def salvar_diagnostico(
    temperatura,
    ram,
    travamentos,
    diagnostico,
    explicacao
):

    conexao = sqlite3.connect(
        "database/techmind.db"
    )

    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO diagnosticos
    (
        data,
        temperatura,
        ram,
        travamentos,
        diagnostico,
        explicacao
    )
    VALUES (?, ?, ?, ?, ?, ?)
    """,
    (
        datetime.now().strftime("%d/%m/%Y %H:%M"),
        temperatura,
        ram,
        travamentos,
        diagnostico,
        explicacao
    ))

    conexao.commit()
    conexao.close()


def listar_historico():

    conexao = sqlite3.connect(
        "database/techmind.db"
    )

    cursor = conexao.cursor()

    cursor.execute("""
    SELECT *
    FROM diagnosticos
    ORDER BY id DESC
    """)

    dados = cursor.fetchall()

    conexao.close()

    return dados

def criar_tabelas():

    conexao = sqlite3.connect(
        "database/techmind.db"
    )

    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS diagnosticos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data TEXT,
        temperatura REAL,
        ram REAL,
        travamentos TEXT,
        diagnostico TEXT,
        explicacao TEXT
    )
    """)

    conexao.commit()
    conexao.close()

def obter_estatisticas():

    conexao = sqlite3.connect(
        "database/techmind.db"
    )

    cursor = conexao.cursor()

    cursor.execute("""
    SELECT diagnostico
    FROM diagnosticos
    """)

    resultados = cursor.fetchall()

    conexao.close()

    total = len(resultados)

    normais = 0

    for item in resultados:

        if item[0] == "Sistema funcionando normalmente":
            normais += 1

    problemas = total - normais

    frequencia = {}

    for item in resultados:

        diagnostico = item[0]

        if diagnostico in frequencia:
            frequencia[diagnostico] += 1
        else:
            frequencia[diagnostico] = 1

    mais_comum = "Nenhum"

    if frequencia:

        mais_comum = max(
            frequencia,
            key=frequencia.get
        )

    return {
        "total": total,
        "normais": normais,
        "problemas": problemas,
        "mais_comum": mais_comum
    }  
def gerar_grafico_diagnosticos():

    conexao = sqlite3.connect(
        "database/techmind.db"
    )

    cursor = conexao.cursor()

    cursor.execute("""
    SELECT diagnostico
    FROM diagnosticos
    """)

    resultados = cursor.fetchall()

    conexao.close()

    frequencia = {}

    for item in resultados:

        diagnostico = item[0]

        if diagnostico in frequencia:
            frequencia[diagnostico] += 1
        else:
            frequencia[diagnostico] = 1

    if len(frequencia) == 0:
        return

    plt.figure(figsize=(8, 5))

    plt.bar(
        list(frequencia.keys()),
        list(frequencia.values())
    )

    plt.title("Diagnósticos Realizados")

    plt.xlabel("Diagnóstico")

    plt.ylabel("Quantidade")

    plt.tight_layout()

    plt.savefig(
        "static/graficos/diagnosticos.png"
    )

    plt.close()