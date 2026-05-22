from colorama import Fore, Style, init
import time

init(autoreset=True)

from interface import entrada_usuario
from diagnostico import (
    analisar_sistema,
    explicar_resultado
)

while True:

    print(Fore.CYAN + "\n" + "=" * 50)
    print(Fore.CYAN + "         TECHMIND - MENU PRINCIPAL")
    print(Fore.CYAN + "=" * 50)

    print(Fore.GREEN + "\n1 - Iniciar diagnóstico")
    print(Fore.YELLOW + "2 - Sobre o sistema")
    print(Fore.RED + "3 - Sair")

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

        print("\n" + "=" * 50)
        print("           DIAGNÓSTICO FINAL")
        print("=" * 50)

        print(Fore.GREEN + f"\nResultado: {resultado}")

        print(Fore.YELLOW + "\nExplicação:")
        print(explicacao)

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

    # SAIR
    elif opcao == "3":

        print(Fore.RED + "\nEncerrando sistema...")
        break

    # OPÇÃO INVÁLIDA
    else:

        print("\nOpção inválida.")