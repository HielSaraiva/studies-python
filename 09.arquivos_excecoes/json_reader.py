# Lendo dados em JSON
from pathlib import Path
import json

path = Path('10.arquivos_excecoes\\numbers.json')
contents = path.read_text()
numbers = json.loads(contents)

print(numbers)