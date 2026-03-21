# __call__ permite chamar uma instância de classe como se fosse uma função.
class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, nome):
        print(nome, 'está chamando', self.phone)
        return 2134


call1 = CallMe('123123123')
retorno = call1('Hiel')
print(retorno)
