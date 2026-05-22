def analisar_sistema(lentidao, temperatura, ram, travamentos):

    if temperatura > 85:
        return "Superaquecimento"

    elif ram > 80:
        return "Uso excessivo de RAM"

    elif travamentos == "sim":
        return "Possível malware"

    elif lentidao == "sim":
        return "Possível gargalo de armazenamento"

    else:
        return "Sistema funcionando normalmente"


def explicar_resultado(resultado):

    explicacoes = {

        "Superaquecimento":
        "A CPU está acima da temperatura ideal.",

        "Uso excessivo de RAM":
        "O consumo de memória está muito alto.",

        "Possível malware":
        "Travamentos podem indicar vírus.",

        "Possível gargalo de armazenamento":
        "HD lento pode causar lentidão.",

        "Sistema funcionando normalmente":
        "Nenhum problema crítico encontrado."
    }

    return explicacoes[resultado]