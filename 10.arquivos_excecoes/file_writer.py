# Escrevendo em um arquivo
from pathlib import Path

path = Path('10.arquivos_excecoes\\script.txt')

contents = 'I love programming.\n'
contents += 'I love creating new games.\n'
contents += 'I love reading new books.\n'

path.write_text(contents)