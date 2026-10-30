for i in range(5):
    print(i)
print("---")

for i in range(1, 6):
    print(i)
print("---")

for i in range(0, 11, 2):
    print(i)
print("---")

for letter in "Python":
    print(letter)

print("Таблица умножения на 7:")
for i in range(1, 11):
    result=7*i
    print(f"7*{i}={result}")

print("Считаем сумму от 1 до 100...")
total=0
for i in range(1,101):
    total=total+i
print(f"Сумма всех чисел от 1 до 100 равна:{total}")