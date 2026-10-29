count=1
while count<=5:
    print("Счет:", count)
    count=count + 1
print("Готово")

while True:   #Бесконечный цикл
    answer=input("Введи слово стоп: ")
    if answer=="стоп":
        break #Выходим из цикла, если ввели "стоп"
print("Вышли из цикла")

timer=10
while timer>=1:
    print("Старт:", timer)
    timer=timer-1
print("Старт!")

while True:
    password=input("Введите пароль:")
    if password=="python123":
        print("Доступ разрешен")
        break
    print("Неверный пароль, попробуйте еще раз")