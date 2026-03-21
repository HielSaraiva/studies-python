import enum

# Direcoes = enum.Enum('Direcoes', ['ESQUERDA', 'DIREITA'])
# print(Direcoes(1), Direcoes['ESQUERDA'], Direcoes.ESQUERDA)

# Melhor usar a classe


# class Direcoes(enum.Enum):
#     ESQUERDA = 1
#     DIREITA = 2

class Direcoes(enum.Enum):
    ESQUERDA = enum.auto()
    DIREITA = enum.auto()


def mover(direcao: Direcoes):
    if not isinstance(direcao, Direcoes):
        raise ValueError('Direção não encontrada')

    print(f'Movendo para {direcao}')


mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
