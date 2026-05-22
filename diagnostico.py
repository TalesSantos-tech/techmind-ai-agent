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
        """
A CPU está operando acima da temperatura ideal.
Isso pode causar:
- queda de desempenho
- desligamentos
- danos ao hardware
        """,

        "Uso excessivo de RAM":
        """
O sistema identificou alto consumo de memória RAM.
Isso pode causar:
- lentidão
- travamentos
- baixo desempenho
        """,

        "Possível malware":
        """
Travamentos frequentes podem indicar:
- vírus
- malware
- processos maliciosos
        """,

        "Possível gargalo de armazenamento":
        """
O armazenamento pode estar limitando o desempenho.
Possíveis causas:
- HD antigo
- pouco espaço
- baixa velocidade de leitura
        """,

        "Sistema funcionando normalmente":
        """
Nenhum problema crítico foi detectado.
O sistema aparenta estar estável.
        """
    }

    return explicacoes[resultado]