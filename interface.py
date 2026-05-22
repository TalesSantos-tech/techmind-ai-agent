def entrada_usuario():

    print("=== TECHMIND ===")

    lentidao = input("O computador está lento? ")
    temperatura = int(input("Temperatura da CPU: "))
    ram = int(input("Uso de RAM (%): "))
    travamentos = input("Há travamentos? ")

    return lentidao, temperatura, ram, travamentos