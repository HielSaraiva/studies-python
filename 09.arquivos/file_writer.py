# Escrevendo em um arquivo
from pathlib import Path
import os

path = Path('script.txt')

contents = 'I love programming.\n'
contents += 'I love creating new games.\n'
contents += 'I love reading new books.\n'

path.write_text(contents)

# Sobrescreve o arquivo
with open(path, 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')

# Continua escrevendo no arquivo (append mode)
with open(path, 'a') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')

# Caso queira ler e escrever, adicione o '+'
with open(path, 'a+') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.seek(0)  # Volta para o início do arquivo
    print(arquivo.read())

# Remove o arquivo
# os.remove(path)

# Renomeia o arquivo
os.rename(path, 'script-renamed.txt')
