# Set (Conjuntos)

# São mutáveis, porém só aceitam tipos imutáveis como valor interno
# s3 = {1, 2, []}  # Erro!
s3 = {1, 2, (123, )}
print(s3)

# Criando set
s1 = set()
print(s1)

s2 = {1, 2, 3, 4, 4, 4, 5}
print(s2)

# Removendo valores duplicados
l1 = [1, 2, 2, 2, 2, 3, 3, 4, 5]
s1 = set(l1)
l2 = list(s1)
print(l2)

# Adicionando valores
s1.add('Hiel')
s1.add(2)
print(s1)

s1.update(('Olá mundo', 6, 7))
print(s1)

# Descartar valor
s1.discard('Hiel')
print(s1)

# Limpar valores
s1.clear()
print(s1)

# Operadores de conjuntos
s1 = {1, 2, 3}
s2 = {2, 3, 4}

s3 = s1 | s2
print(s3)
s3 = s1 & s2
print(s3)
s3 = s1 - s2
print(s3)
s3 = s1 ^ s2
print(s3)
