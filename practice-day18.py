# Задача №1
def say_hello():
    print("Привет, мир")
say_hello()

# Задача №2
def greet_user(name):
    print(f"Привет, {name}!")
greet_user("Анна")
greet_user("Олег")

# Задача №3
def double(number):
    print(number*2)
double(5)
double(10)
double(2)

# Задача №4
def countdown(start):
    for i in range(start, 0, -1):
        print(i)
    print("Поехали!")
countdown(3)
countdown(5)

# Задача №5
def draw_triangle(rows):
    for i in range(1, rows +1):
        print("*" * i)
draw_triangle(3)
draw_triangle(5)
draw_triangle(10)

# Задача 6
def print_even_numbers(limit):
    for i in range(1, limit+1):
        if i%2==0:
            print(i)
print_even_numbers(10)

# Задача 7
def repeat_word(word, count):
    for i in range(count):
        print(word)
repeat_word("Python", 3)

# Задача 8
def calculate_average(numbers_list):
    if len(numbers_list)==0:
        print("Список пуст")
    else:
        average=sum(numbers_list)/len(numbers_list)
        print(f"Среднее арифмитическое: {average}")
calculate_average([10, 20, 30])
calculate_average([])