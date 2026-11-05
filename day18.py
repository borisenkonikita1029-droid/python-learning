def greet():
    print("Привет!")
    print("Рад тебя видеть")
# Вызов функции
greet()
greet()

def greet_person(name):
    print(f"Привет, {name}!")

# Вызов функции с аргументом
greet_person("Анна")
greet_person("Олег")

def line():
    print("-" * 20)
line()
def show_square(n):
    print(f"Квадрат: {n**2}")
show_square(5)
line()
show_square(10)