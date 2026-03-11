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


# Multiplas listas
carros_disponiveis = ['argo', 'hb20', 'hilux', 'ferrari', 'porsche', 'cronos']

carros_pedidos = ['argo', 'hb20']

for carros_pedido in carros_pedidos:
    if carros_pedido in carros_disponiveis:
        print(f"Adicionando {carros_pedido}")
    else:
        print(f"Desculpe, não temos!")

# Operador ternário (if else de uma linha)
condicao = 10 == 11
variavel = 'Valor' if condicao else 'Outro valor'
print(variavel)


# Guard Clause - Evitando uso repetitivo de if
def calcular_desconto(preco, cliente_vip):
    # Guard clauses
    if preco <= 0:
        return "Preço inválido"

    if not cliente_vip:
        return preco

    # Código principal (só chega aqui se passou nas validações)
    return preco * 0.9


print(calcular_desconto(124, True))
