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


p1 = Ponto(1, 2)
p2 = Ponto(978, 876)

print(p1)
print(p2)


# Funções decoradoras
def adiciona_repr(cls):
    def meu_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr
    cls.__repr__ = meu_repr
    return cls


@adiciona_repr
class Time:
    def __init__(self, nome):
        self.nome = nome


t1 = Time('Brasil')
print(t1)
