class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Representação amigável
    def __str__(self):
        # class_name = self.__class__.__name__
        return f'({self.x}, {self.y})'

    # Representação presica, técnica
    def __repr__(self):
        # class_name = self.__class__.__name__
        class_name = type(self).__name__
        return f'{class_name}(x={self.x}, y={self.y})'

    # Define o comportamento do operador +
    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Ponto(novo_x, novo_y)

    # Define o comportamento de self > other
    def __gt__(self, other):
        resultado_self = self.x + self.y
        resultado_other = other.x + other.y
        return resultado_self > resultado_other


p1 = Ponto(1, 2)
p2 = Ponto(6, 4)
p3 = p1 + p2
print(p3)
print(p1 > p2)
