from dog import *
from golden import *


my_dog = Dog('Bolt', 6)
print(f"My dog's name is {my_dog.name}")

my_dog.roll_over()
my_dog.sit()

my_new_dog = Golden('Flock', 5)
print(f"My dog's name is {my_new_dog.name}")