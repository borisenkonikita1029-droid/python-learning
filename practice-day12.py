number=int(input("Введите число для таблицы умножения:"))
for i in range(1,11):
    result=number*i
    print(f"{number}*{i}={result}")

total=0
for i in range(1, 51):
    total=total+i
print(f"Сумма всех чисел = {total}")

number=int(input("Введите любое число"))
for i in range(number, 0, -1):
    print(i)
print("Поехали")

count=int(input("Сколько чисел вы хотите ввести?"))
maximum=0
for i in range(count):
    number=int(input("Введите число"))
    if number>maximum:
        maximum=number
print(f"Самое большое число это {maximum}")
