# Introducao às Listas

# Lista com vários tipos de dados
import sys


lista1 = [123, 1.2, True, 'Hiel', [], ()]
print(lista1)

# Lista é um tipo mutável
lista1[3] = "Geni"
print(lista1)

# Acessando elementos
pessoas = ['hiel', 'alanis', 'conrado']

print(pessoas)
print(pessoas[0].title())
print(pessoas[-1].title())

# Adicionando elementos a uma lista
pessoas.append('charles')  # adiciona no final da lista
print(pessoas)

pessoas.insert(0, 'pimenta')  # adiciona na posicao indicada
print(pessoas)

# Removendo elementos de uma lista
del pessoas[0]  # remove o elemento por meio do índice
print(pessoas)

# remove do final da lista, como se fosse o topo de uma pilha, e retorna o valor removido
pessoa_popped = pessoas.pop()
print(pessoa_popped)

# remove de uma posicao especifica e retorna o valor removido
primeira_pessoa_popped = pessoas.pop(0)
print(primeira_pessoa_popped)

print(pessoas)
# nao retorna o valor removido, mas remove sem a necessidade de usar o indice
pessoa_removida = pessoas.remove('alanis')
print(pessoa_removida)
print(pessoas)

# Ordenando listas
pessoas = ['hiel', 'alanis', 'conrado', 'charles', 'ryan', 'pimenta']
pessoas.sort()  # afeta a ordem original da lista
print(pessoas)
pessoas.sort(reverse='True')
print(pessoas)

ordenada = sorted(pessoas)  # nao afeta a ordem original da lista
print(ordenada)

# nao afeta a ordem original da lista
desordenada = sorted(pessoas, reverse='True')
print(desordenada)

# Invertendo listas
print(f"-> {pessoas}")
pessoas.reverse()  # afeta a ordem original da lista
print(f"-> {pessoas}")

# Identificando tamanho da lista
print(len(pessoas))

# Concatenando e estendendo listas
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
print(lista_c)
lista_d = [7, 8, 9]
lista_c.extend(lista_d)
print(lista_c)

# Cuidados com dados mutáveis
lista_a = ['Hiel', 'Geni']
lista_b = lista_a  # Passando a referência (ponteiros)

lista_a[0] = 'Oi'
print(lista_b)

lista_a = ['Hiel', 'Geni']
lista_b = lista_a.copy()

lista_a[0] = 'Oi'
print(lista_b)

# Empacotamento e desempacotamento
nome1, nome2, nome3 = ['Hiel', 'Geni', 'Queiroga']
print(nome2)

nome1, *_ = ['Hiel', 'Geni', 'Queiroga']
print(nome1, _)

# Enumerate - enumera iteráveis (índices)
lista = ['Maria', 'Helena', 'Luiz']

iterator = enumerate(lista)
print(iterator)

lista_enumerada = list(iterator)

print(lista_enumerada)

for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])

# Iteráveis dentro de Iteráveis
salas = [
    ['Maria', 'Helena'],
    ['Hiel'],
    ['Deus'],
]
print(salas[0])
print(salas[0][1])

# List comprehension
lista = [i for i in range(10)]
print(lista)

lista = [2*i + 1 for i in range(10)]
print(lista)

lista = [
    (x, y)
    for x in range(4)
    for y in range(3)
]
print(lista)

# Filter
lista = [i for i in range(10) if i < 5]
print(lista)

# Generator expression
lista = [n for n in range(1000000)]
# Uma função que pausa e chama os valores sequencialmente
generator = (n for n in range(1000000))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))  # Não está na memória.
