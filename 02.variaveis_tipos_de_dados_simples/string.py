# Strings

# Variável de escape
print("Hiel \"Saraiva")

# r -> é usado para expressões regulares
print(r"Hiel \"Saraiva")

# Aspas simples e duplas
print("Hiel 'Saraiva'")

# Formatando Strings
name = "hiel saraiva"
print(name.title())

name = "HIEL SARAIVA"
print(name.title())

name = "hiel saraiva"
print(name.upper())
print(name.lower())

first_name = "geni"
last_name = "saraiva"
full_name = f"{first_name} {last_name}"  # f-strings
print(full_name)
print(full_name[0])
print(full_name[1])
print(full_name[2])
print(full_name[3])
print(full_name[-1])
print(full_name[-2])
print(full_name[-3])

print(f"Olá, {full_name.title()}!")

surra = 12
print(f"Vai doido, tome peia pra {surra}")

altura = 1.8
print(f"Tenho {altura:.2f}m de altura")

a = "A"
b = "B"
c = 1.1
formato = "a={} b={} c={:.2f}".format(a, b, c)
print(formato)

formato = "a={0} b={1} c={2:.2f}".format(a, b, c)
print(formato)

formato = "a={letra1} b={letra2} c={letra3:.2f}".format(
    letra1=a, letra2=b, letra3=c)
print(formato)

nome = 'Hiel'
preco = 100.10231
idade = 12
variavel = '%s, o preço é R$%f.2f' % (nome, preco)  # Interpolação
print('tenho %d anos' % (idade))
print(variavel)

# Espacamentos
print("\tSalte")
print("\nQuebre linha")

favorite_language = " python "
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())
print(favorite_language)

nome = 'Hiel'
print(f"{nome}")
print(f"{nome: >10}")
print(f"{nome: <10}.")
print(f"{nome:$^10}.")

# Prefixo
url = "https://qacademico.com.br"
simple_url = url.removeprefix("https://")
print(simple_url)
print(simple_url.removesuffix(".com.br"))

print("One of Python's strngths is its diverse community.")
# print('One of Python's strngths is its diverse community.') error

# Fatiamento de Strings
variavel = "Olá mundo!!!"
print(variavel[4:])
print(variavel[4:7])
print(variavel[4:7:2])  # o último parâmetro é o passo

# Quantidade de caracteres
print(len(variavel))

# Iterando uma string
texto = 'Hiel'  # iterável
iteratador = iter(texto)  # iterator

while True:
    try:
        print(next(iteratador), end='')
    except StopIteration:
        break

# Dividindo e unindo strings
frase = 'É o Laion'
lista_palavras = frase.split()
print(lista_palavras)

frases_unidas = ' '.join(lista_palavras)
print(frases_unidas)
