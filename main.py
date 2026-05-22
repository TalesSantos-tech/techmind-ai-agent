from interface import entrada_usuario
from diagnostico import (
    analisar_sistema,
    explicar_resultado
)

# Entrada
lentidao, temperatura, ram, travamentos = entrada_usuario()

# Processamento
resultado = analisar_sistema(
    lentidao,
    temperatura,
    ram,
    travamentos
)

# Explicação
explicacao = explicar_resultado(resultado)

# Saída
print("\n" + "=" * 50)
print("           DIAGNÓSTICO FINAL")
print("=" * 50)

print(f"\nResultado: {resultado}")

print("\nExplicação:")
print(explicacao)

print("=" * 50)