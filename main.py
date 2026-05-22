from interface import entrada_usuario
from diagnostico import (
    analisar_sistema,
    explicar_resultado
)

lentidao, temperatura, ram, travamentos = entrada_usuario()

resultado = analisar_sistema(
    lentidao,
    temperatura,
    ram,
    travamentos
)

explicacao = explicar_resultado(resultado)

print("\nDiagnóstico Final:")
print(resultado)

print("\nExplicação:")
print(explicacao)