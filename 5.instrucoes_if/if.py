# Instrucoes if

# Verificacoes multiplas
idade_0 = 18
idade_1 = 12
print(idade_0 > 0 and idade_1 < 0)

idade_0 = 18
idade_1 = 12
print(idade_0 > 0 or idade_1 < 0)

# Veficando se um valor já/nao está na lista
comidas = ['arroz', 'feijao', 'macarrao', 'miojo']
print('miojo' in comidas)
print('arroz' not in comidas)

# Expressoes booleanas
vida_status = True
morte_status = False

# Elif
if idade_0 != 18:
    print("Hello World!")
elif 'miojo' in comidas:
    print("Mopa!")

# Verificando se uma lista esta vazia
carros = []

if carros:
    print("Possui carros")
else:
    print("Está vazia")
