# Input e While

# input()
message = input("Me diga algo e eu repetirei de volta: ") # Tudo é interpretado como string
print(message)

# Usando int()
prompt_1 = "Bem-vindo ao sistema de idades"
prompt_1 += "\nQual a sua idade? "
idade = int(input(prompt_1)) # Converte para inteiro
print(idade >= 18)

# While
pets = ['dog', 'cat', 'dog', 'dog', 'hamster']
print(pets)

while 'dog' in pets:
    pets.remove('dog')

print(pets)
