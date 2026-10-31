# Повторение дней 10-11 вместо мини-проектов
#Задачи по дню 10
age=int(input("Введите свой возраст"))
tickets=input("Есть ли у вас билет (да или нет)?")
if age>=18 and tickets=="да":
    print("Проходите в зал")
else:
    print("Вход запрещен")

card=input("Есть ли у вас карта лояльности (да/нет)")
amount=int(input("На какую сумму вы совершили покупки?"))
if card=="да" or amount>1000:
    print("Скидка 5%")
else:
    print("Скидки нету")

is_workday=input("Сегодня рабочий день? (да/нет)")
if not (is_workday=="да"):
    print("Отдыхаем!")
else:
    print("Работаем")

#задачи по дню 11
secret="777"
while True:
    code=input("Введите код")
    if code==secret:
        print("Замок открыт!")
        break
    else:
        print("Неверный код")

total=0
while total<20:
    number=int(input("Введите число"))
    total=total+number
    print("Текущая сумма", total)
