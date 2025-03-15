# Trabalhando com listas

# Percorrer elementos de uma lista
pessoas = ['Hiel', 'Alanis', 'Conrado', 'Charles', 'Pimenta']

for pessoa in pessoas:
    print(f"{pessoa.title()}, parabéns! Você teve o seu TCC aprovado!")

# Criando uma lista de numeros
numeros = list(range(1, 10)) # nao conta o 10
print(numeros)

numeros_pares = list(range(2, 20, 2))
print(numeros_pares)

numeros_quadrados = []
for numero in range(1, 15):
    numeros_quadrados.append(numero ** 2)
print(numeros_quadrados)

numeros_quadrados = [numero ** 2 for numero in range(1, 15)] # List comprehensions
print(numeros_quadrados)

# Estatistica simples
print(min(numeros))
print(max(numeros))
print(sum(numeros))

# Fatias de listas
print(pessoas[1:2]) 
print(pessoas[-3:])

# Copia de uma lista
copia_pessoas = pessoas[:]
# copia_pessoas = pessoas # nao copia, mas referencia a mesma lista

# Tuplas: listas imutaveis
dimensoes_retangulo = (200, 120)
print(dimensoes_retangulo)

dimensoes_retangulo = (250, 120)
print(dimensoes_retangulo)
