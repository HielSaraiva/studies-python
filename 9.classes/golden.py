from dog import *

class Golden(Dog):

    def __init__(self, name, age):
        super().__init__(name, age)
        self.cor = 'amarelo'
        