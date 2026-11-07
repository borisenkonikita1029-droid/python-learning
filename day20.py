# Задача 1
temperatures = [15, 22, 8, 30, 18]
for temp in temperatures:
    if temp>20:
        print(temp)

# Задача 2
prices = {"хлеб": 40, "молоко": 80, "сыр": 200}
def find_price(product_name):
    return prices.get(product_name, "Нет в наличии")
print(find_price("хлеб"))
print(find_price("мясо"))

# Задача 3
students = [
    {"name": "Анна", "grade": 4},
    {"name": "Олег", "grade": 5},
    {"name": "Мария", "grade": 3}
]
def get_excellent_students(students_list):
    high_grades=[]
    for student in students_list:
        if student["grade"]==5:
            high_grades.append(student["name"])
    return high_grades
print(get_excellent_students(students))

# Найти ошибку в задаче
total = 0
while True:
    num = int(input("Введи число (0 для выхода): "))
    if num == 0:
        break
    total += num
print(f"Сумма: {total}")

# Для понимания
fruits = ["яблоко", "банан", "вишня", "груша", "слива"]

def find_a_fruits(fruits_list):
    result = []  # 1. Коробка для результата
    
    for fruit in fruits_list:  # 2. Берем по одному фрукту
        if "а" in fruit:       # 3. Проверяем, есть ли буква "а"
            result.append(fruit) # 4. Если есть — кладем в коробку
            
    return result  # 5. Отдаем коробку (вне цикла!)