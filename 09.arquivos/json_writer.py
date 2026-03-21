import json

pessoa = {
    'nome': 'Hiel',
    'sobrenome': 'Saraiva',
    'enderecos': [
        {'rua': 'Rio Negro', 'numero': 290}
    ],
    'dev': True
}

with open('test.json', 'w') as arquivo:
    json.dump(pessoa, arquivo, indent=3)
