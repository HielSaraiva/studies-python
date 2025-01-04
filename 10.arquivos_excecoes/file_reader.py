# Lendo de arquivos
from pathlib import Path

path = Path('10.arquivos_excecoes\\pi_digits.txt')
contents = path.read_text()
contents = contents.rstrip() # remove a linha em branco ao final do arquivo
# contents = path.read_text().rstrip() # outra forma
print(contents[:50])

# Separando as linhas
lines = contents.splitlines()
# for line in lines:
#     print(line)

# Juntando as linhas em uma só string
pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[:50])
print(len(pi_string))

# Verificando se uma string está contida
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print('Your birthday appears in the first million digits of pi!')
else:
    print('Your birthday does not appears in the first million digits of pi!')

