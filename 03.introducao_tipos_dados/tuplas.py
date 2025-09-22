# Introdução às tuplas

# Tupla é um tipo imutável
tupla1 = (123, True, 'Hiel')
print(tupla1)

# Criando tupla
minha_tupla = ('maçã', 'banana', 'cereja')
minha_tupla = 'maçã', 'banana', 'cereja'
print(minha_tupla)

print(minha_tupla[1])

# Printando elemento a elemento
for i in minha_tupla:
    print(i)

print(len(minha_tupla))

# Criando uma tupla com apenas um item
tupla1 = ('hiel',)
print(tupla1)

# ALgumas operações
print(minha_tupla.count('maçã'))
print(minha_tupla.index('banana'))
