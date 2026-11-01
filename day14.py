# Проект 1: Игра "Угадай число"
import random
secret=random.randint(1,100)
attemps=0
while True:
    attemps=attemps+1
    number=int(input("Введите число"))
    if number<secret:
        print("Загаданное число больше")
    elif number>secret:
        print("Загаданное число меньше")
    else:
        print(f"Вы угадали число {secret} за {attemps} попыток")
        break

# Проект 2: "Калькулятор с меню"
while True:
    print("1-Сложение")
    print("2-Вычетание")
    print("3-Умножение")
    print("4-Деление")
    print("0-Выход")
    action=int(input("Какое действие вы хотите выполнить?"))
    if action==0:
        print("Досвидания!")
        break
    if action==1:
        number_1=float(input("Введите первое число"))
        number_2=float(input("Введите второе число"))
        result=number_1+number_2       
        print(f"Результат сложения равен {result}")
    if action==2:
        number_1=float(input("Введите первое число"))
        number_2=float(input("Введите второе число"))
        result=number_1-number_2
        print(f"Результат вычетания равен {result}")
    if action==3:
        number_1=float(input("Введите первое число"))
        number_2=float(input("Введите второе число"))
        result=number_1*number_2
        print(f"Результат умножения равен {result}")
    if action==4:
        number_1=float(input("Введите первое число"))
        number_2=float(input("Введите второе число"))
        result=number_1/number_2
        print(f"Результат деления равен {result}")