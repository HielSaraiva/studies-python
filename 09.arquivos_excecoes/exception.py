# Trabalhando com excecoes

# Bloco try-except and else
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        # caso nao queira fazer nada, use "pass"
        print("You can't divide by 0!")
    else:  # caso não ocorra erro
        print(answer)


# Try, except, else e finally
try:
    a = 18
    b = 0
    c = a / b

except ZeroDivisionError:
    print('Não é permitido dividir por zero')
except (TypeError, IndexError) as error:
    print("TypeError and IndexError")
    print('MSG', error)
    print('Nome', error.__class__.__name__)
except Exception:
    print('Erro desconhecido')
finally:  # sempre será executado
    print('Fim do bloco')


# Lançando exceções
def divide(n, d):
    try:
        return n/d
    except ZeroDivisionError:
        raise  # relançar o erro
