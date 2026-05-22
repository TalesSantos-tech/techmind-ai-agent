import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

import tkinter as tk
from tkinter import messagebox

from diagnostico import (
    analisar_sistema,
    explicar_resultado
)


# FUNÇÃO PRINCIPAL
def executar_diagnostico():

    lentidao = entrada_lentidao.get()
    temperatura = int(entrada_temperatura.get())
    ram = int(entrada_ram.get())
    travamentos = entrada_travamentos.get()

    resultado = analisar_sistema(
        lentidao,
        temperatura,
        ram,
        travamentos
    )

    explicacao = explicar_resultado(resultado)

    texto_resultado.config(
        text=f"{resultado}\n\n{explicacao}"
    )


# JANELA
janela = tk.Tk()

janela.title("TechMind AI")
janela.geometry("600x500")

# TÍTULO
titulo = tk.Label(
    janela,
    text="TECHMIND - AI PC DIAGNOSTIC",
    font=("Arial", 16, "bold")
)

titulo.pack(pady=20)

# LENTIDÃO
tk.Label(
    janela,
    text="Computador está lento? (sim/nao)"
).pack()

entrada_lentidao = tk.Entry(janela)
entrada_lentidao.pack()

# TEMPERATURA
tk.Label(
    janela,
    text="Temperatura da CPU"
).pack()

entrada_temperatura = tk.Entry(janela)
entrada_temperatura.pack()

# RAM
tk.Label(
    janela,
    text="Uso de RAM (%)"
).pack()

entrada_ram = tk.Entry(janela)
entrada_ram.pack()

# TRAVAMENTOS
tk.Label(
    janela,
    text="Há travamentos? (sim/nao)"
).pack()

entrada_travamentos = tk.Entry(janela)
entrada_travamentos.pack()

# BOTÃO
botao = tk.Button(
    janela,
    text="ANALISAR SISTEMA",
    command=executar_diagnostico,
    bg="blue",
    fg="white",
    font=("Arial", 12, "bold")
)

botao.pack(pady=20)

# RESULTADO
texto_resultado = tk.Label(
    janela,
    text="Resultado aparecerá aqui",
    font=("Arial", 11),
    wraplength=500,
    justify="left"
)

texto_resultado.pack(pady=20)

# EXECUTAR
janela.mainloop()