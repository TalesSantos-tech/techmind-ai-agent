def entrada_usuario():

    print("=" * 50)
    print("      TECHMIND - AI PC DIAGNOSTIC")
    print("=" * 50)

    lentidao = input("\nO computador está lento? (sim/nao): ")

    temperatura = int(
        input("Temperatura média da CPU (°C): ")
    )

    ram = int(
        input("Uso de RAM (%): ")
    )

    travamentos = input(
        "Há travamentos frequentes? (sim/nao): "
    )

    return lentidao, temperatura, ram, travamentos