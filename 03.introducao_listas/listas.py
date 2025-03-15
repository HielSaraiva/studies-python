# Introducao às Listas

# Acessando elementos
pessoas = ['hiel', 'alanis', 'conrado']

print(pessoas)
print(pessoas[0].title())
print(pessoas[-1].title())

# Adicionando elementos a uma lista
pessoas.append('charles') # adiciona no final da lista
print(pessoas)

pessoas.insert(0, 'pimenta') # adiciona na posicao indicada
print(pessoas)

# Removendo elementos de uma lista
del pessoas[0] # remove o elemento por meio do índice 
print(pessoas)

pessoa_popped = pessoas.pop() # remove do final da lista, como se fosse o topo de uma pilha, e retorna o valor removido
print(pessoa_popped)

primeira_pessoa_popped = pessoas.pop(0) # remove de uma posicao especifica e retorna o valor removido
print(primeira_pessoa_popped)

print(pessoas)
pessoa_removida = pessoas.remove('alanis') # nao retorna o valor removido, mas remove sem a necessidade de usar o indice
print(pessoa_removida)
print(pessoas)

# Ordenando listas
pessoas = ['hiel', 'alanis', 'conrado', 'charles', 'ryan', 'pimenta']
pessoas.sort() # afeta a ordem original da lista
print(pessoas)
pessoas.sort(reverse='True')
print(pessoas)

ordenada = sorted(pessoas) # nao afeta a ordem original da lista
print(ordenada) 

desordenada = sorted(pessoas, reverse='True') # nao afeta a ordem original da lista
print(desordenada) 

# Invertendo listas
print(f"-> {pessoas}")
pessoas.reverse() # afeta a ordem original da lista
print(f"-> {pessoas}")

# Identificando tamanho da lista
print(len(pessoas))