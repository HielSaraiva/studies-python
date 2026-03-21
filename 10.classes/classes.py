from dataclasses import dataclass
from abc import ABC, abstractmethod


# Construtor da Classe
class Pessoa:
    # Construtor
    def __init__(self, nome, sobrenome):  # Self remete a própria instância (como o this do Java)
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa('Hiel', 'Saraiva')
p2 = Pessoa('Geni', 'Saraiva')

print(p1.nome)
print(p1.sobrenome)
print(p2.nome)
print(p2.sobrenome)


# Métodos em instâncias de classes
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        print(f'{self.modelo} está acelerando!')


argo = Carro('Fiat', 'Argo 2025')
print(argo.marca)
argo.acelerar()


# Atributos de Classe
class Pessoa:
    ano_atual = 2026

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade


p1 = Pessoa('Hiel', 25)
print(Pessoa.ano_atual)
print(p1.get_ano_nascimento())


# __dict__ e vars() para atributos de instância
print(p1.__dict__)
print(vars(p1))


# Métodos de classes
class Pessoa:
    ano_atual = 2026

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print("Hey")

    @classmethod  # Fábrica
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)


p1 = Pessoa('João', 34)
p2 = Pessoa.criar_com_50_anos('Helena')

print(p2.nome, p2.idade)


# Métodos Estásticos
class Classe:

    @staticmethod
    def funcao_que_esta_na_classe(*args, **kwargs):
        print('Oi', args, kwargs)


c1 = Classe()
c1.funcao_que_esta_na_classe(1, 2, 3)

Classe.funcao_que_esta_na_classe(nomeado=1)


# @property - um getter no modo pythônico
class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    @property  # Um método que se comporta como um atributo
    def cor(self):
        return self.cor_tinta

    @property
    def cor_tampa(self):
        return 123456


caneta = Caneta('Azul')
print(caneta.cor)


# @property + @setter
# Atributos que começam com um ou dois
# _ não devem ser usados fora da classe
class Caneta:
    def __init__(self, cor):
        self._cor = cor

    @property  # Um método que se comporta como um atributo
    def cor(self):
        return self._cor

    @cor.setter
    def cor(self, valor):
        if valor == 'Rosa':
            raise ValueError('Não aceito essa cor!')
        self._cor = valor


caneta = Caneta('Azul')
print(caneta.cor)


# Encapsulamento
class Foo:
    def __init__(self):
        self.public = 'Isso é público'
        self._protected = 'Isso é protegido'  # Apenas as classes e as subclasses
        self.__private = 'Isso é privado'  # Apenas a classe

    def metodo_publico(self):
        return 'metodo_publico'

    def _metodo_protegido(self):
        return '_metodo_protegido'

    def __metodo_privado(self):
        return '__metodo_privado'


teste = Foo()

print(teste.metodo_publico())
print(teste._metodo_protegido())
# print(teste.__metodo_privado())


# Associação - Um objeto usa outro, mas sem dependência forte
class Professor:
    def __init__(self, nome):
        self.nome = nome

    def ensinar(self, aluno):
        print(f'{self.nome} está ensinando {aluno.nome}')


class Aluno:
    def __init__(self, nome):
        self.nome = nome


prof = Professor('Carlos')
aluno = Aluno('Maria')
prof.ensinar(aluno)


# Agregação - Uma classe contém outra, mas ela pode existir independentemente
class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)


class Funcionario:
    def __init__(self, nome):
        self.nome = nome


depto = Departamento('TI')
func = Funcionario('João')
depto.adicionar_funcionario(func)
print(f'{func.nome} trabalha em {depto.nome}')


# Composição - Uma classe contém outra de forma integral (forte dependência)
class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.coracao = Coracao()  # Criado aqui, morrem juntos

    def viver(self):
        self.coracao.bater()


class Coracao:
    def bater(self):
        print('Tum-tum... Tum-tum...')


pessoa = Pessoa('Ana')
pessoa.viver()


# Herança Simples
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Aluno(Pessoa):
    ...


a1 = Aluno("Hiel", "Saraiva")
a1.falar_nome_classe()


# super() e a sobreposição de métodos
class MinhaString(str):
    def upper(self):
        print("Chamou Upper")
        return super().upper()


string = MinhaString("Luiz")
print(string.upper())


class A:
    atributo_a = "A"

    def __init__(self, atributo):
        self.atributo = atributo


class B(A):
    atributo_b = "B"

    def __init__(self, atributo):
        super().__init__(atributo)


class C(B):
    atributo_c = "C"

    def __init__(self, atributo):
        super().__init__(atributo)


# Herança Múltipla
# Problema do Diamante
#        A
#      /   \
#     B     C
#      \   /
#        D
# Python 3 usa C3 superclass linearization para gerar o mro (method resolution order)
# Para saber a ordem de chamada dos métodos, use o método de classe Classe.mro()
# Ou o atributo __mro__ (Dunder - Double Underscore)


class A:
    ...

    def quem_sou(self):
        print('A')


class B(A):
    ...

    def quem_sou(self):
        print('B')


class C(A):
    ...

    def quem_sou(self):
        print('C')


class D(B, C):
    ...

    # def quem_sou(self):
    #     print('D')


d = D()
d.quem_sou()
print(D.mro())


# Classes Abstratas
# Para criar uma classe abstrata é preciso extender de ABC e ter ao menos um método abstrato
class Log(ABC):
    @abstractmethod
    def _log(self, msg):
        ...

    def log_error(self, msg):
        return self._log(f"Error: {msg}")

    def log_success(self, msg):
        return self._log(f"Success: {msg}")


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')


# l = Log()  # Vai gerar erro

l = LogPrintMixin()
l.log_error("Erro")


# Abstract Method para qualquer método já decorado
class AbstractFoo(ABC):
    def __init__(self, name):
        self._name = name

    @property
    @abstractmethod
    def name(self):
        pass


class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


foo = Foo("Bar")
print(foo.name)


# Polimorfismo, assinatura de métodos e Liskov Substitution Principle
# SO'L'ID (Objetos de uma superclasse devem ser substituíveis por objetos de uma subclasse sem quebrar a aplicação)
# Sobrecarga de métodos = Python não suporta
# Sobreposição de métodos = Python suporta
class Notificacao(ABC):
    def __init__(self, mensagem):
        self._mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool:
        pass


class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print('E-mail: enviando - ', self._mensagem)
        return True


class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print('SMS: enviando - ', self._mensagem)
        return True


def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print("Notificação enviada!")
    else:
        print("Notificação não enviada!")


notificar(NotificacaoEmail('Testando email'))
notificar(NotificacaoSMS('Testando SMS'))


# Metaclasses
# O tipo de uma classe em Python é "type"
# O objeto é uma instância da classe
# A classe é uma instância de type (type é uma metaclass)
# Ao criar uma classe, coisas ocorrem por padrão nessa ordem:
# __new__ da metaclass é chamado e cria a nova classe
# __call__ da metaclass é chamado com os argumentos e chama:
# __new__ da class com os argumentos (cria a instância)
# __init__ da class com os argumentos
# __call__ da metaclass termina a execução


# Dataclasses - São syntax sugar para criar classes normais
@dataclass
class Pessoa:
    nome: str
    sobrenome: str


p1 = Pessoa("Hiel", 'Saraiva')
print(p1)
p2 = Pessoa('Hiel', 'Saraiva')
print(p1 == p2)
print(p1.__eq__(p2))
