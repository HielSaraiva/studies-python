# Input e While

# input()
# Tudo é interpretado como string
message = input("Me diga algo e eu repetirei de volta: ")
print(message)

message = input("Me diga algo e eu repetirei de volta: ")
print(f"{message=}")

# Usando int()
prompt_1 = "Bem-vindo ao sistema de idades"
prompt_1 += "\nQual a sua idade? "
idade = int(input(prompt_1))  # Converte para inteiro
print(idade >= 18)

# While
pets = ['dog', 'cat', 'dog', 'dog', 'hamster']
print(pets)

while 'dog' in pets:
    pets.remove('dog')

print(pets)

contador = 0
while contador <= 100:
    contador += 4

    if contador == 60:
        print("Não vou mostrar o 60")
        continue

    if contador >= 70 and contador <= 80:
        print("Não vou mostrar o ", contador)
        continue

    print(contador)

    if contador == 90:
        break
