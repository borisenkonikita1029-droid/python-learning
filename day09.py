age=int(input("Сколько тебе лет?"))
if age>=18:
    print("Ты совершеннолетний")
else:
    print("Ты еще не совершеннолетний")
print("Конец программы")

number=int(input("Введите любое число"))
if number%2==0:
    print("Число четное")
else:
    print("Число нечетное")

password=input("Введите ваш пароль")
if password=="python":
    print("Добро пожаловать")
else:
    print("Доступ закрыт")

number=int(input("Введите любое число"))
if number>0:
    print("Ваше число положительное")
elif number<0:
    print("Ваше число отрицательное")
else:
    print("Ваше число это ноль")