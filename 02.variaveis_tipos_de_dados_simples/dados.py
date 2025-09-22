# Dados

# Coerção de tipos
from itertools import combinations, permutations, product
print(int('1') + 1)
print(int('1'), type(int('1')))

print(str(12) + '3')

print(bool(1), type(bool(1)))

# Concatenação e repetição
concatenacao = "Hiel" + " " + "Saraiva"
print(concatenacao)

a_dez_vezes = "A" * 10
print(a_dez_vezes)

# Identidade de um valor na memória
v1 = 'a'
v2 = 'a'
v3 = v2
print(id(v1))
print(id(v2))
print(id(v3))

"""
Dados mutáveis: [], {}, set()
Dados imutáveis: (), "", 0, 0.0, None, False, range(0, 10)
"""


# Variáveis nonlocal
def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar=''):
        nonlocal valor_final  # Procura no escopa acima
        valor_final += valor_a_concatenar
        return valor_final
    return interna


c = concatenar('a')


# Combinação, permutação e produto cartesiano
pessoas = [
    'Hiel', 'Joana', 'Luiz',
]

camisetas = [
    ['preta', 'branca']
]

print('Combinação')
for i in combinations(pessoas, 2):
    print(i)

print('\nPermutação')
for i in permutations(pessoas, 2):
    print(i)

print('\nProduto')
for i in product(pessoas, *camisetas):
    print(i)
