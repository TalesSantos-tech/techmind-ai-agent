import sqlite3


def conectar():

    conexao = sqlite3.connect(
        "database/techmind.db"
    )

    return conexao


def criar_tabelas():

    conexao = conectar()

    cursor = conexao.cursor()

    # TABELA USUÁRIOS
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        nome TEXT NOT NULL,

        email TEXT NOT NULL,

        senha TEXT NOT NULL
    )
    """)

    # TABELA DIAGNÓSTICOS
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS diagnosticos (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        resultado TEXT,

        explicacao TEXT
    )
    """)

    conexao.commit()

    conexao.close()