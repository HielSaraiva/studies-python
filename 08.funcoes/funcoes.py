# Funcoes

# Argumentos nomeados
from functools import reduce
from itertools import count


def describe_pet(animal_type, pet_name):
    """Exibe as informacoes sobre um animal"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(animal_type='hamster', pet_name='hiel')


# Argumentos defaults
def describe_pet(pet_name, animal_type='dog'):
    """Exibe as informacoes sobre um animal"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(pet_name='hiel')


# Numero arbitrario de argumentos
def make_pizza(*toppings):  # Uma tupla é criada
    print(toppings)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers')


# Argumentos não nomeados variaveis
def soma(*args):  # empacota em uma tupla
    total = 0
    for numero in args:
        total += numero
    return total


print(soma(1, 2, 3, 4, 5, 6, 7, 8))
print(sum((1, 2, 3, 4, 5, 6, 7, 8)))


# Argumentos nomeados arbitrarios
def build_profile(first, last, **user_info):  # empacota em um dicionário
    """Cria um dicionario contendo tudo o que sabemos sobre um usuario"""
    user_info['first_name'] = first  # Esses valores sao adicionados após os argumentos arbitrarios
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('hiel', 'saraiva', location='fortaleza')
print(user_profile)


# Closure e Funções que retornam outras funções
def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar  # Fechamento


falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

print(falar_bom_dia('Luiz'))
print(falar_boa_noite('Luiz'))


# Funções Lambdas
def x(a): return a + 10


print(x(5))


def minha_funcao(n):
    return lambda a: a * n


duplicar = minha_funcao(2)
print(duplicar(11))


# Termos técnicos
"""
Higher Order Functions: Funções que recebem ao menos uma função como parâmetro e retornam outra função

First-Class Functions: Funções que são tratadas como qualquer outra variável (str, int, float, etc).
"""


# Importando um modulo inteiro
"""
import nome_modulo # Singleton
"""

# Importando funcoes especificas
"""
from nome_modulo import nome_funcao_1, nome_funcao_2
"""

# Usando 'as' para atribuir um alias a uma funcao
"""
from nome_modulo import nome_funcao_1 as nf1
"""

# Usando 'as' para atribuir um alias a um modulo
"""
import nome_modulo as nm
"""

# Importando todas as funcoes de um modulo
"""
from nome_modulo import * 
"""

# Recarregando módulos
"""
import importlib

importlib.reload(<nome do modulo>)
"""

# Entendendo os módulos
"""
- O primeiro módulo executado chama-se __main__
- o python não reconhece pastas e módulos acima do __main__ padrão
"""

"""
__init__.py é um arquivo de inicialização dos packages
"""


# Generator
def generator(n=0):
    yield 1  # Pausar
    print('Continuando...')
    yield 2  # Pausar
    print('Mais uma vez...')
    yield 3
    print('Vou terminar')
    return 'Acabou'


gen = generator(n=0)
# print(next(gen))
# print(next(gen))

for n in gen:
    print(n)


# Yield from
def gen1():
    yield 1
    yield 2
    yield 3


def gen2():
    yield from gen1()
    yield 4
    yield 5
    yield 6


g = gen2()
for n in g:
    print(n)


# Funções decoradoras
def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            e_string(arg)
            resultado = func(*args, **kwargs)
            print('Ok, agora você foi decorada')
        return resultado
    return interna


@criar_funcao  # Decorador
def inverte_string(string):
    print('Inverte String')
    return string[::-1]


def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')


# inverte_string_checando_parametro = criar_funcao(inverte_string)
# invertida = inverte_string_checando_parametro(123)
invertida = inverte_string('123')
print(invertida)


# Count é um iterador sem fim

c1 = count()
r1 = range(10)

print('count')
for i in c1:
    if i >= 100:
        break
    print(i)

print('range')
for i in r1:
    print(i)


# Map
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def quadrado(x):
    return x * x


resultados = map(quadrado, numeros)
lista_resultados = list(resultados)

print(lista_resultados)


# Filter
def eh_par(x):
    return x % 2 == 0


pares = filter(eh_par, lista_resultados)

lista_pares = list(pares)
print(lista_pares)


# Reduce
def soma(x, y):
    return x + y


resultado = reduce(soma, lista_resultados)
print(resultado)


# Recursão
# import sys
# sys.setrecursionlimit(1000)

def recursiva(inicio=0, fim=10):
    if inicio >= fim:
        return fim
    inicio += 1
    return recursiva(inicio, fim)


print(recursiva())


# Problema dos parâmetros mutáveis
def adicionar_clientes(nome, lista=[]):
    lista.append(nome)
    return lista


client1 = adicionar_clientes('Hiel')
print(client1)

client2 = adicionar_clientes('Geni')
print(client2)


# Positional Only-Parameters (tudo antes da '/' dever ser apenas posicional)
def soma(a, b, /, x, y):
    print(a + b + x + y)


soma(1, 2, y=2, x=1)
