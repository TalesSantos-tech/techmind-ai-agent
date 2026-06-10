def analisar_sistema(lentidao, temperatura, ram, travamentos):

    # =========================
    # NORMALIZAÇÃO SEGURA
    # =========================

    try:
        temperatura = float(temperatura)
    except:
        temperatura = 0

    try:
        ram = float(ram)
    except:
        ram = 0

    lentidao = str(lentidao).strip().lower()
    travamentos = str(travamentos).strip().lower()

    # =========================
    # LÓGICA ORIGINAL (MANTIDA)
    # =========================

    if temperatura > 85:
        return "Superaquecimento"

    elif ram > 85:
        return "Uso excessivo de RAM"

    elif travamentos == "sim":
        return "Possível malware"

    elif lentidao == "sim":
        return "Possível gargalo de armazenamento"

    elif ram > 70:
        return "RAM elevada"

    else:
        return "Sistema funcionando normalmente"


def explicar_resultado(resultado):

    explicacoes = {

        "RAM elevada":
        """
A utilização de memória está acima do ideal.

Ainda não é crítica, mas pode indicar:
- muitos programas abertos
- navegador consumindo memória
- necessidade de mais RAM
""",

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

    return explicacoes.get(
        resultado,
        "Resultado desconhecido. Sem explicação disponível."
    )