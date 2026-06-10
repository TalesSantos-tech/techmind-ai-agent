from interface import entrada_usuario
from diagnostico import (
    analisar_sistema,
    explicar_resultado
)

from banco import (
    criar_tabelas,
    salvar_diagnostico,
    listar_historico
)

from colorama import Fore, Style, init
from datetime import datetime
import time

init(autoreset=True)

from banco import criar_tabelas
criar_tabelas()


def salvar_historico(resultado, explicacao):

    data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    with open(
        "logs/historico.txt",
        "a",
        encoding="utf-8"
    ) as arquivo:

        arquivo.write("=" * 50 + "\n")
        arquivo.write(f"Data: {data}\n")
        arquivo.write(f"Resultado: {resultado}\n")
        arquivo.write(f"Explicação: {explicacao}\n")
        arquivo.write("=" * 50 + "\n\n")

def salvar_metricas(resultado):

    with open(
        "logs/metricas.txt",
        "a",
        encoding="utf-8"
    ) as arquivo:

        arquivo.write(resultado + "\n")

while True:

    print(Fore.CYAN + "\n" + "=" * 50)
    print(Fore.CYAN + "         TECHMIND - MENU PRINCIPAL")
    print(Fore.CYAN + "=" * 50)

    print(Fore.GREEN + "\n1 - Iniciar diagnóstico")
    print(Fore.YELLOW + "2 - Sobre o sistema")
    print(Fore.MAGENTA + "3 - Ver histórico")
    print(Fore.BLUE + "4 - Ver métricas")
    print(Fore.RED + "5 - Sair")
    opcao = input("\nEscolha uma opção: ")

    # DIAGNÓSTICO
    if opcao == "1":

        lentidao, temperatura, ram, travamentos = entrada_usuario()

        print(Fore.BLUE + "\nAnalisando sistema...")
        time.sleep(2)

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

        print("\n" + "=" * 50)
        print("           DIAGNÓSTICO FINAL")
        print("=" * 50)

        print(Fore.GREEN + f"\nResultado: {resultado}")

        print(Fore.YELLOW + "\nExplicação:")
        print(explicacao)

        salvar_historico(resultado, explicacao)
        salvar_metricas(resultado)

        print("=" * 50)

    # SOBRE
    elif opcao == "2":

        print("\n" + "=" * 50)
        print("                SOBRE")
        print("=" * 50)

        print("""
TechMind é um agente inteligente desenvolvido
em Python capaz de identificar possíveis
problemas em computadores com base
nos sintomas informados pelo usuário.
        """)

    # HISTÓRICO
    elif opcao == "3":

        historico = listar_historico()

        print(Fore.MAGENTA + "\n" + "=" * 50)
        print(Fore.MAGENTA + " HISTÓRICO DE DIAGNÓSTICOS ")
        print(Fore.MAGENTA + "=" * 50)

        if len(historico) == 0:

            print("\nNenhum diagnóstico encontrado.")

        else:

            for item in historico:

                print("\nID:", item[0])
                print("Data:", item[1])
                print("Temperatura:", item[2])
                print("RAM:", item[3])
                print("Travamentos:", item[4])
                print("Diagnóstico:", item[5])

                print("-" * 40)
        # MÉTRICAS
    elif opcao == "4":

        try:

            with open(
                "logs/metricas.txt",
                "r",
                encoding="utf-8"
            ) as arquivo:

                linhas = arquivo.readlines()

                total = len(linhas)

                normais = linhas.count(
                    "Sistema funcionando normalmente\n"
                )

                problemas = total - normais

                taxa = (
                    (total / total) * 100
                    if total > 0 else 0
                )

                print(Fore.BLUE + "\n" + "=" * 50)
                print(Fore.BLUE + "              MÉTRICAS")
                print(Fore.BLUE + "=" * 50)

                print(f"\nTotal de diagnósticos: {total}")

                print(
                    f"Problemas detectados: {problemas}"
                )

                print(
                    f"Sistemas normais: {normais}"
                )

                print(
                    f"Taxa de funcionamento: {taxa:.0f}%"
                )

        except FileNotFoundError:

            print("\nArquivo de métricas não encontrado.")
            
    # Sair
    elif opcao == "5":

        print(Fore.RED + "\nEncerrando sistema...")
        break

    # OPÇÃO INVÁLIDA
    else:

        print("\nOpção inválida.")