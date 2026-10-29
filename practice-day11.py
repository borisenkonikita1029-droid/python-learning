# Копилка
total_1=0
while total_1<100:
    total_2=int(input("Введите сумму которую хотите ложить в копилку:"))
    total_1=total_1+total_2
    print("в копилке:", total_1)
print("Вы накопили 100! Молодец!")

# Надоедливый робот
while True:
    print("Привет! Как дела?")
    answer=input("Ответь роботу: ")
    if answer=="пока":
        print("Робот обиделся и ушел")
        break

# Угадай число
secret=7
attempts=0
while True:
    guess=int(input("Введите число"))
    attempts=attempts+1
    if guess==secret:
        print(f"Ты угадал число за {attempts} попыток ")
        break
    elif guess<secret:
        print("Загаданное число больше")
    elif guess>secret:
        print("Загаданное число меньше")

# Банкомат
balance=1000
while True:
    action=input("Выберите действие снять или выйти: ")
    if action=="снять":
        money=int(input("Введите сумму которую хотите снять"))
        if money>balance:
            print("Недостаточно средств")
        else:
            balance=balance-money
            print(f"Вы сняли {money}. Остаток на счету: {balance}")
    elif action=="выйти":
        print("До свидания!")
        break
    else:
         print("Неизвестная команда")