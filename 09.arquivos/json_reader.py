import json

with open('test.json', 'r') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)
    print(type(pessoa))
