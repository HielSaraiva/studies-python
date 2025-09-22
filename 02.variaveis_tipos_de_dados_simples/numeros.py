# Numeros
import decimal

# Inteiros
print(2 + 3)
print(2 * 3)
print(2 - 3)
# sempre float, qualquer outra operacao entre int e float vai resultar em float
print(2 / 3)
print(2 // 3)  # Corta as casas decimais
print(2 ** 3)
print(55 % 2)
print("")

# Floats
print(2.0 + 3.0)
print(2.0 * 3.0)
print(2.0 - 3.0)
print(2.0 / 3.0)
print(2.0 // 3.0)
print(2.0 ** 3.0)
print(55.0 % 2.0)
print("")

# Underscores em numeros
universe_age = 14_000_000_000  # serve para inteiros e floats
print(universe_age)
print("")

# Atribuicao multipla
x, y, z = 0, 0, 0

# Constantes
MAX_APPLES = 5000  # não possui constantes built-in

# Imprecisão de números de ponto flutuante (não é exclusivo do python)
numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.2f}')
print(round(numero_3, 2))

numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.2f}')
print(round(numero_3, 2))
