# Strings

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
full_name = f"{first_name} {last_name}"
print(full_name)

print(f"Olá, {full_name.title()}!")

# Espacamentos
print("\tSalte")
print("\nQuebre linha")

favorite_language = " python "
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())
print(favorite_language)

# Prefixo
url = "https://qacademico.com.br"
simple_url = url.removeprefix("https://")
print(simple_url)
print(simple_url.removesuffix(".com.br"))

print("One of Python's strngths is its diverse community.")
#print('One of Python's strngths is its diverse community.') error