# Funcoes

# Argumentos nomeados
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
def make_pizza(*toppings): # Uma tupla é criada
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers')

# Argumentos nomeados arbitrarios
def build_profile(first, last, **user_info):
    """Cria um dicionario contendo tudo o que sabemos sobre um usuario"""
    user_info['first_name'] = first # Esses valores sao adicionados após os argumentos arbitrarios
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('hiel', 'saraiva', location='fortaleza')
print(user_profile)

# Importando um modulo inteiro
"""
import nome_modulo
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