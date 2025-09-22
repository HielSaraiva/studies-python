# Dicionarios
import copy as cp

# Dicionario simples
alien_0 = {'cor': 'verde',
           'pontos': 5}
print(alien_0['cor'])

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Dicionario vazio
alien_0 = {}

alien_0 = {'cor': 'verde',
           'pontos': 5}
print(alien_0['cor'])

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Modificando valores em um dicionario
alien_0['cor'] = 'azul'
print(alien_0)

# Removendo pares chave-valor
del alien_0['pontos']
print(alien_0)

cor = alien_0.pop('cor')
print(cor)
print(alien_0)

ultima_chave = alien_0.popitem()
print(ultima_chave)
print(alien_0)

alien_0.update({
    'pontos': 5,
    'cor': 'verde',
})

print(alien_0)

# Usando get()
pontos = alien_0.get('pontos', 'Não há um valor de pontos')
print(pontos)

# Percorrendo todos os pares chave-valor
user_0 = {
    'usuario': 'hiel11',
    'nome': 'hiel',
    'sobrenome': 'saraiva',
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

# Percorrendo todas as chaves de um dicionario
for k in user_0.keys():
    print(k.title())

# for k in user_0:      # Seria a mesma coisa, pois é o comportamento padrao
#     print(k.title())

# Percorrendo as chaves de um dicionario com um loop em uma ordem especifica
for k in sorted(user_0.keys()):
    print(k.title())

# Percorrendo todos os valores de um dicionario
for k in user_0.values():  # Possui repeticoes
    print(k.title())

for k in set(user_0.values()):  # Não possui repeticoes
    print(k.title())

# Lista de dicionarios
alien_0 = {'cor': 'verde', 'pontos': 5}
alien_1 = {'cor': 'amarelo', 'pontos': 10}
alien_2 = {'cor': 'vermelho', 'pontos': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)


aliens = []

for alien_number in range(30):
    new_alien = {'cor': 'vermelho', 'pontos': 5 * (alien_number + 1)}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)

# Lista em um dicionario
linguagens_favoritas = {
    'hiel': ['c', 'java', 'python'],
    'alanis': ['c', 'python'],
}

for name, languages in linguagens_favoritas.items():
    print(f"\n{name.title()}'s favorite languages are: ")
    for language in languages:
        print(f"\t{language.title()}")

# Dicionario em um dicionario
usuarios = {
    'hiel11': {
        'nome': "hiel",
        'sobrenome': 'saraiva',
        'nacionalidade': 'brasileiro',
    },

    'xaxa123': {
        'nome': 'anaxágoras',
        'sobrenome': None,
        'nacionalidade': 'brasileiro',
    },
}

print(usuarios)


# Quantidade de chaves
print(len(linguagens_favoritas))


# Colocando valor padrão em uma chave
user_0.setdefault('idade', 0)
print(user_0['idade'])


# Shallow copy x Deep copy
d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}
d2 = d1.copy()  # Copia apenas valores imutáveis e linkam os mutáveis

d2['c1'] = 1000
d2['l1'][1] = 99999

print(d1)
print(d2)


d3 = cp.deepcopy(d1)
d3['l1'][1] = 1

print(d3)

# Ordenação
lista = [
    {'nome': 'Hiel', 'sobrenome': 'Freitas'},
    {'nome': 'Geni', 'sobrenome': 'Saraiva'},
    {'nome': 'Augusto', 'sobrenome': 'Soares'},
]

# Recebe o nome para comparar
l1 = sorted(lista, key=lambda item: item['nome'])

print(l1)


# Empacotando e desempacotando dicionários
pessoa = {
    'nome': 'Hiel',
    'sobrenome': 'Souza',
}
(a1, a2), (b1, b2) = pessoa.items()
print(a1, a2)
print(b1, b2)

dados_pessoa = {
    'idade': 16,
    'altura': 1.6
}

pessoa_completa = {**pessoa, **dados_pessoa}
print(pessoa_completa)

# *args (um asterisco) coleta argumentos posicionais em uma tupla.

# **kwargs (dois asteriscos) coleta argumentos nomeados em um dicionário.


def mostro_argumentos_nomeados(*args, **kwargs):
    print(kwargs)


mostro_argumentos_nomeados(nome='Joana', qlq=123)


# Dictionary Comprehension
dc = {
    chave: valor
    for chave, valor
    in dados_pessoa.items()
}

print(dc)
