from diagnostico import analisar_sistema


def test_superaquecimento():

    resultado = analisar_sistema(
        "sim",
        95,
        40,
        "nao"
    )

    assert resultado == "Superaquecimento"


def test_ram():

    resultado = analisar_sistema(
        "nao",
        50,
        95,
        "nao"
    )

    assert resultado == "Uso excessivo de RAM"


def test_malware():

    resultado = analisar_sistema(
        "nao",
        50,
        40,
        "sim"
    )

    assert resultado == "Possível malware"


def test_sistema_normal():

    resultado = analisar_sistema(
        "nao",
        50,
        40,
        "nao"
    )

    assert resultado == "Sistema funcionando normalmente"