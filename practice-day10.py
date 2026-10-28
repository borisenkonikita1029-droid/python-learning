# Задача 1 "Светофор"
color=input("Введите любой цвет светофора")
if color=="Красный":
    print("Стоп")
elif color=="Желтый":
    print("Приготовься")
elif color=="Зеленый":
    print("Иди")
else:
    print("Такого цвета нет")
# Задача 2 "Строгий вход"
login=input("Введите свой логин")
password=input("Введите свой пароль")
if (login=="admin") and (password=="1234"):
    print("Добро пожаловать в систему")
else:
    print("Неверный логин или пароль")
# Задача 3 "Оценка фильма"
rating=int(input("Дайте оценку этому фильму от 1 до 10"))
if rating==10:
    print("Шедевр")
elif rating==8 or rating==9:
    print("Отличный фильм")
elif (rating>=5) and (rating<=7):
    print("Неплохо")
else:
    print("Лучше не смотреть")