from interface import entrada_usuario
from diagnostico import (
    analisar_sistema,
    explicar_resultado
)

while True:

    print("\n" + "=" * 50)
    print("         TECHMIND - MENU PRINCIPAL")
    print("=" * 50)

    print("\n1 - Iniciar diagnóstico")
    print("2 - Sobre o sistema")
    print("3 - Sair")

    opcao = input("\nEscolha uma opção: ")

    # DIAGNÓSTICO
    if opcao == "1":

        lentidao, temperatura, ram, travamentos = entrada_usuario()

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

        print(f"\nResultado: {resultado}")

        print("\nExplicação:")
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

        print("\nEncerrando sistema...")
        break

    # OPÇÃO INVÁLIDA
    else:

        print("\nOpção inválida.")