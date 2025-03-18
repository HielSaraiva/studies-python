# Dicionarios

# Dicionario simples
alien_0 = {'cor': 'verde', 'pontos': 5}
print(alien_0['cor'])

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Dicionario vazio
alien_0 = {}

alien_0 = {'cor': 'verde', 'pontos': 5}
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
for k in user_0.values(): # Possui repeticoes
    print(k.title())

for k in set(user_0.values()): # Não possui repeticoes
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

