import matplotlib.pyplot as plt


def gerar_grafico():

    try:

        with open(
            "logs/metricas.txt",
            "r",
            encoding="utf-8"
        ) as arquivo:

            linhas = [
                linha.strip()
                for linha in arquivo.readlines()
            ]

        categorias = {
            "Superaquecimento": 0,
            "Uso excessivo de RAM": 0,
            "Possível malware": 0,
            "Possível gargalo de armazenamento": 0,
            "Sistema funcionando normalmente": 0
        }

        for linha in linhas:

            if linha in categorias:
                categorias[linha] += 1

        nomes = list(categorias.keys())
        valores = list(categorias.values())

        plt.figure(figsize=(10, 5))

        plt.bar(nomes, valores)

        plt.title(
            "Diagnósticos do TechMind"
        )

        plt.xlabel("Categorias")
        plt.ylabel("Quantidade")

        plt.xticks(rotation=10)

        plt.tight_layout()

        plt.savefig(
            "dashboard/grafico_metricas.png"
        )

        plt.show()

    except FileNotFoundError:

        print(
            "Arquivo de métricas não encontrado."
        )


gerar_grafico()