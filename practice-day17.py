grades={"Математика": 4, "История": 5, "Физика": 3, "Химия": 3, "Литература": 5}
print("Математика:", grades["Математика"], "Литература:", grades["Литература"])
grades["Информатика"]=5
total=0
count=0
for subject, grade in grades.items():
    total+=grade
    count+=1
average=total/count
print(f"Средняя оценка: {round(average, 2)}")
print(grades)

expenses={"Париж": 150, "Лондон": 200, "Берлин": 80, "Рим": 120}
total=0
count=0
for city,expen in expenses.items():
    total+=expen
    count+=1
average=total/count
print(f"Общая сумма: {total}, Всего городов: {count}, Средний расход: {average}")

shopping_list=["Яблоки", "Хлеб", "Молоко", "Яйца"]
prices={"Яблоки": 50, "Хлеб": 40, "Молоко": 80, "Яйца": 70, "Сыр": 200}
total_cost=0
for product in shopping_list:
    price=prices[product]
    total_cost+=price
print(f"Итого к оплате: {total_cost} рублей")