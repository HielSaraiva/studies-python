# __new__ vs __init__
# __new__: Cria o objeto na memória (alocação)
# __init__: Inicializa os atributos do objeto já criado
# Ordem: __new__ é chamado PRIMEIRO, depois __init__
# Quem chama __init__? Python chama automaticamente após __new__ retornar

class A:
    def __new__(cls, *args, **kwargs):
        # __new__ cria a instância vazia (pré-inicialização)
        # Retorna o objeto criado
        print('Chamando __new__')
        instancia = super().__new__(cls)
        return instancia  # Python pega esse objeto e chama __init__ nele

    def __init__(self, x):
        # __init__ recebe o objeto já criado e inicializa seus atributos
        # Não retorna nada (retorna None implicitamente)
        print('Chamando __init__')
        self.x = x

    def __repr__(self):
        return 'A()'


a = A(123)
print(a.x)
