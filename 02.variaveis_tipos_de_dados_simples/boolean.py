# Boolean

# Verificando tipo de dados
print(type("Olá Mundo!!"))
print(type(20))
print(type(3.12))
print(type(10 == 10))

# Valores booleanos
print(10 > 9)
print(10 >= 9)
print(10 != 9)
print(10 == 9)
print(10 < 9)
print(10 <= 9)
print()

# Função bool() para avaliar qualquer valor booleano
x = 0
y = 1
z = "Olá Mundo"
k = ""
l1 = [1, 2, 3]
l2 = []

print(bool(x))  # Qualquer número diferente de 0 é True
print(bool(y))
print(bool(k))  # Qualquer string não vazia é True
print(bool(z))
print(bool(l2))  # Qualquer lista, tupla, set, dicionário não vazio é True
print(bool(l1))
print(bool(None))

"""
Se houver uma classe com a função __len__ retornando 0 ou false, a função bool avaliará-la como False.
"""

"""
Valores que são considerados falsos:
lista = []
dicionario = {}
conjunto = set()
tupla = ()
string = ''
inteiro = 0
flutuante = 0.0
nada = None
falso = False
intervalo = range(0)
"""
