# Type hints são anotações que indicam quais tipos uma função/variável aceita
from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from functools import wraps
from typing import ClassVar
from typing import TypeVar, Generic
from typing import (
    List, Dict, Tuple, Set, Optional, Union, Callable, Any,
    TypeAlias, Final, Literal, Protocol, TypedDict, overload, cast
)


# ANOTAÇÕES BÁSICAS
# Variáveis simples
nome: str = "João"
idade: int = 25
altura: float = 1.80
ativo: bool = True
nada: None = None


# Função com anotações
def saudar(nome: str) -> str:
    """Recebe string, retorna string"""
    return f"Olá, {nome}!"


print(saudar("Maria"))


# TIPOS COMPOSTOS (COLLECTIONS)
# Lista de inteiros
numeros: List[int] = [1, 2, 3]

# Dicionário (chave: string, valor: inteiro)
idades: Dict[str, int] = {"João": 30, "Maria": 25}

# Tupla com tipos específicos
coordenada: Tuple[int, int] = (10, 20)

# Conjunto de strings
cores: Set[str] = {"vermelho", "azul", "verde"}


# OPTIONAL E UNION
# Optional[X] = X | None (pode ser X ou None)
def encontrar_usuario(id: int) -> Optional[str]:
    """Retorna nome ou None se não encontrar"""
    if id == 1:
        return "João"
    return None


# Union: pode ser um tipo OU outro
def processar_valor(valor: Union[int, str]) -> str:
    """Aceita int ou str"""
    if isinstance(valor, int):
        return f"Número: {valor}"
    return f"Texto: {valor}"


# Python 3.10+: Sintaxe com | (PEP 604)
def processar_modernos(valor: int | str) -> str:
    """Versão Python 3.10+"""
    if isinstance(valor, int):
        return f"Número: {valor}"
    return f"Texto: {valor}"


# TYPE ALIASES (Apelidos para tipos)
# Criando apelidos (Python 3.9)
Usuario = Dict[str, Union[str, int]]

usuario1: Usuario = {"nome": "João", "idade": 30}

# Python 3.12+: TypeAlias explícito (melhor prática)
IdUsuario: TypeAlias = int
NomeUsuario: TypeAlias = str


def buscar_usuario(id: IdUsuario) -> NomeUsuario:
    return "João" if id == 1 else "Desconhecido"


# CALLABLE (Funções como tipos)
# Função que recebe outra função
def executar_callback(callback: Callable[[int, int], int]) -> int:
    """
    Callable[[param1, param2, ...], retorno]
    Recebe função que toma 2 ints e retorna int
    """
    return callback(5, 3)


def somar(a: int, b: int) -> int:
    return a + b


resultado = executar_callback(somar)
print(f"Resultado callback: {resultado}")


# LITERAL (Valores específicos permitidos)
# Apenas os valores específicos são aceitos
def defini_tema(tema: Literal["claro", "escuro", "auto"]) -> None:
    """Tema pode ser apenas uma dessas 3 opções"""
    print(f"Tema definido: {tema}")


defini_tema("claro")
# defini_tema("rosa")  # Erro de type checking


# FINAL (Não pode ser alterado)
# Constante - não pode ser reatribuída
VERSAO_APP: Final = "1.0.0"
MAX_TENTATIVAS: Final[int] = 3


# Método que não pode ser sobrescrito
class Animal:
    @Final
    def fazer_som(self) -> None:
        """Método final, não pode ser sobrescrito"""
        print("Som")


# TYPEDDICT (Dicionário com campos tipados)
# Requer Python 3.8+
class UsuarioDados(TypedDict):
    """Define a estrutura esperada do dicionário"""
    nome: str
    idade: int
    email: str


def processar_usuario(dados: UsuarioDados) -> str:
    """Agora o editor sabe os campos do dicionário"""
    return f"{dados['nome']} ({dados['idade']})"


usuario_data: UsuarioDados = {"nome": "João",
                              "idade": 30, "email": "joao@email.com"}
print(processar_usuario(usuario_data))


# CAST (Conversão de tipo para o type checker)
def obter_dados() -> Any:
    return {"nome": "João"}


# Cast diz ao type checker que é uma string
dados = cast(Dict[str, str], obter_dados())
# Agora o editor sabe que 'dados' é Dict[str, str]


# GENÉRICOS (Generic Types)
# TypeVar: variável de tipo genérica
T = TypeVar("T")


class Caixa(Generic[T]):
    """Caixa que pode guardar qualquer tipo"""

    def __init__(self, conteudo: T):
        self.conteudo = conteudo

    def obter(self) -> T:
        return self.conteudo


caixa_int: Caixa[int] = Caixa(42)
caixa_str: Caixa[str] = Caixa("Hello")

print(f"Caixa 1: {caixa_int.obter()}")
print(f"Caixa 2: {caixa_str.obter()}")


# CONSTRAINTS (Limitar tipos genéricos)
# T_numero só pode ser int ou float
T_numero = TypeVar("T_numero", int, float)


def dobrar(valor: T_numero) -> T_numero:
    """Funciona com int ou float, retorna o mesmo tipo"""
    return valor * 2  # type: ignore


# ANY (Tipo genérico - qualquer coisa)
def processar_qualquer_coisa(valor: Any) -> Any:
    """Any significa: qualquer tipo é aceito, retorna qualquer tipo"""
    return valor


# TYPE CHECKING EM RUNTIME
def verificar_tipo(valor: int) -> None:
    """Runtime verification"""
    if not isinstance(valor, int):
        raise TypeError(f"Esperava int, recebeu {type(valor)}")
    print(f"✓ É um int: {valor}")


verificar_tipo(42)
# verificar_tipo("texto")  # Erro em runtime


# VARIÂNCIA (Covariance e Contravariance)
# Covariance: ListaCovariante[Subclasse] é subclasse de ListaCovariante[Classe]
# Contravariance: Função que aceita Classe é "maior" que função que aceita Subclasse

# Exemplo: List é covariante em Python 3.9+
class Animal:
    pass


class Cachorro(Animal):
    pass


animais: List[Animal] = [Cachorro()]  # Funciona: Cachorro é Animal


# VARIÁVEIS COM TIPOS COMPLEXOS
# Callback que não recebe argumentos e não retorna nada
callback_simples: Callable[[], None] = lambda: print("Callback!")
callback_simples()

# Dicionário de listas de tuplas
dados_complexos: Dict[str, List[Tuple[int, str]]] = {
    "grupo1": [(1, "um"), (2, "dois")],
    "grupo2": [(3, "três"), (4, "quatro")]
}

# Função que retorna função


def criar_multiplicador(n: int) -> Callable[[int], int]:
    """Retorna uma função que multiplica por n"""
    def multiplicador(x: int) -> int:
        return x * n
    return multiplicador


mult_por_3 = criar_multiplicador(3)
print(f"10 * 3 = {mult_por_3(10)}")


# CLASS VARIABLES VS INSTANCE VARIABLES
class Configuracao:
    # Variável de classe (compartilhada)
    versao: ClassVar[str] = "1.0"

    # Variáveis de instância
    nome: str
    valor: int

    def __init__(self, nome: str, valor: int):
        self.nome = nome
        self.valor = valor


# DECORADORES COM TYPE HINTS
def meu_decorador(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorador com type hints"""
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Chamando {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Resultado: {result}")
        return result
    return wrapper


@meu_decorador
def soma_decorada(a: int, b: int) -> int:
    return a + b


soma_decorada(5, 3)


# TYPE HINTS EM CLASSES
class Pessoa:
    """Exemplo completo de type hints em classe"""

    # Atributo de classe
    contador_instancias: ClassVar[int] = 0

    # Atributos de instância (com tipos)
    nome: str
    idade: int
    cpf: Optional[str]
    telefones: List[str]

    def __init__(self, nome: str, idade: int, cpf: Optional[str] = None) -> None:
        """Construtor com anotações"""
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.telefones: List[str] = []
        Pessoa.contador_instancias += 1

    def adicionar_telefone(self, telefone: str) -> None:
        """Adiciona telefone à lista"""
        self.telefones.append(telefone)

    def obter_nome_completo(self) -> str:
        """Retorna nome formado"""
        return self.nome.upper()

    def fazer_aniversario(self) -> None:
        """Incrementa idade"""
        self.idade += 1

    def __str__(self) -> str:
        """Representação em string"""
        return f"{self.nome} ({self.idade} anos)"

    def __repr__(self) -> str:
        """Representação técnica"""
        return f"Pessoa(nome='{self.nome}', idade={self.idade})"

    @property
    def eh_maior_idade(self) -> bool:
        """Property com retorno tipado"""
        return self.idade >= 18

    @staticmethod
    def validar_idade(idade: int) -> bool:
        """Método estático com tipos"""
        return 0 <= idade <= 150

    @classmethod
    def criar_de_dicionario(cls, dados: Dict[str, str]) -> "Pessoa":
        """Factory method com type hints"""
        return cls(
            nome=dados.get("nome", "Desconhecido"),
            idade=int(dados.get("idade", 0)),
            cpf=dados.get("cpf")
        )


# Usando a classe
pessoa1 = Pessoa("João Silva", 30, "123.456.789-00")
pessoa1.adicionar_telefone("11999999999")

print(f"Pessoa: {pessoa1}")
print(f"Nome: {pessoa1.obter_nome_completo()}")
print(f"É maior de idade? {pessoa1.eh_maior_idade}")

# Usando factory method
dados = {"nome": "Maria", "idade": "25", "cpf": None}
pessoa2 = Pessoa.criar_de_dicionario(dados)
print(f"Criada de dict: {pessoa2}")


# HERANÇA COM TYPE HINTS
class Veiculo:
    """Classe base"""

    def __init__(self, marca: str, modelo: str) -> None:
        self.marca = marca
        self.modelo = modelo

    def descrever(self) -> str:
        return f"{self.marca} {self.modelo}"


class Carro(Veiculo):
    """Subclasse com type hints"""

    def __init__(self, marca: str, modelo: str, portas: int) -> None:
        super().__init__(marca, modelo)
        self.portas: int = portas

    def descrever(self) -> str:
        # Override com mesmo tipo de retorno
        return f"{super().descrever()} ({self.portas} portas)"


carro = Carro("Fiat", "Argo", 4)
print(f"Carro: {carro.descrever()}")


# ABSTRACT BASE CLASSES COM TYPE HINTS
class Animal(ABC):
    """Classe abstrata com type hints"""

    nome: str

    def __init__(self, nome: str) -> None:
        self.nome = nome

    @abstractmethod
    def fazer_som(self) -> str:
        """Método abstrato que retorna string"""
        pass

    def info(self) -> str:
        """Método concreto com tipo"""
        return f"{self.nome}: {self.fazer_som()}"


class Gato(Animal):
    """Implementação concreta"""

    def fazer_som(self) -> str:
        return "Miau!"


class Cachorro(Animal):
    """Outra implementação concreta"""

    def fazer_som(self) -> str:
        return "Au au!"


animais: List[Animal] = [
    Gato("Whiskers"),
    Cachorro("Rex")
]

for animal in animais:
    print(animal.info())


# DATACLASSES COM TYPE HINTS
@dataclass
class Ponto:
    """Dataclass com type hints automáticos"""
    x: float
    y: float
    rotulo: str = "origem"  # Valor padrão


@dataclass
class Retangulo:
    """Dataclass com tipos complexos"""
    superior_esquerdo: Ponto
    inferior_direito: Ponto
    vertices: List[Ponto] = field(default_factory=list)

    def calcular_area(self) -> float:
        """Calcula área do retângulo"""
        width = self.inferior_direito.x - self.superior_esquerdo.x
        height = self.superior_esquerdo.y - self.inferior_direito.y
        return abs(width * height)


ponto1 = Ponto(0, 10, "superior")
ponto2 = Ponto(10, 0, "inferior")
retangulo = Retangulo(ponto1, ponto2)

print(f"Ponto 1: {ponto1}")
print(f"Área: {retangulo.calcular_area()}")


# SELF-REFERENCING TYPES
class Node:
    """Nó que referencia a si mesmo"""

    def __init__(self, valor: int, proximo: Optional["Node"] = None) -> None:
        self.valor = valor
        self.proximo = proximo

    def append(self, valor: int) -> "Node":
        """Retorna a própria classe"""
        if self.proximo is None:
            self.proximo = Node(valor)
        else:
            self.proximo.append(valor)
        return self

    def listar(self) -> List[int]:
        """Lista todos os valores"""
        valores = [self.valor]
        if self.proximo:
            valores.extend(self.proximo.listar())
        return valores


node = Node(1).append(2).append(3)
print(f"Linked list: {node.listar()}")


# MÉTODO COM MÚLTIPLOS RETORNOS
class ResultadoOperacao:
    """Representa sucesso ou falha"""

    def __init__(self, sucesso: bool, mensagem: str, dados: Any = None):
        self.sucesso = sucesso
        self.mensagem = mensagem
        self.dados = dados


def operacao_que_pode_falhar(valor: int) -> ResultadoOperacao:
    """Retorna tipo customizado indicando sucesso/falha"""
    if valor < 0:
        return ResultadoOperacao(False, "Valor não pode ser negativo")
    return ResultadoOperacao(True, "Operação realizada", valor * 2)


resultado = operacao_que_pode_falhar(5)
print(f"Sucesso: {resultado.sucesso}, Dados: {resultado.dados}")


# SLOTS COM TYPE HINTS
class PessoaOtimizada:
    """Usar __slots__ economiza memória"""
    __slots__: List[str] = ["nome", "idade"]

    nome: str
    idade: int

    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade


# __slots__ previne adicionar atributos dinâmicos
pessoa_otimizada = PessoaOtimizada("João", 30)
# pessoa_otimizada.novo_atributo = "erro"  # Erro!


# DESCRIPTOR COM TYPE HINTS
class TemperaturaCelsius:
    """Descriptor que valida temperatura"""

    def __init__(self, nome: str) -> None:
        self.nome = nome
        self._valor = 0.0

    def __get__(self, obj: Any, objtype: Any = None) -> float:
        return self._valor

    def __set__(self, obj: Any, valor: float) -> None:
        if valor < -273.15:
            raise ValueError("Temperatura abaixo do zero absoluto!")
        self._valor = valor


class Termometro:
    """Classe usando descriptor"""
    temperatura: TemperaturaCelsius = TemperaturaCelsius("temperatura")

    def __init__(self, temp_inicial: float) -> None:
        self.temperatura = temp_inicial


termometro = Termometro(25.0)
print(f"Temperatura: {termometro.temperatura}°C")
