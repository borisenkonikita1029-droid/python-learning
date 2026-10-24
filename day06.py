# мини-проект "анкета"
name=input("Введите ваше имя")
age=int(input("Ваш возраст?"))
city=input("Ваш город?")
print("---ВАША АНКЕТА---")
print(f"Имя: {name}")
print(f"возраст: {age}")
print(f"Город: {city}")
# мини-проект "калькулятор"
number_1=float(input("Назовите первое число"))
number_2=float(input("Назовите второе число"))
amount=number_1+number_2
difference=number_1-number_2
work=number_1*number_2
private=number_1/number_2
print(f"Сумма= {amount}")
print(f"Разность= {difference}")
print(f"Произведение= {work}")
print(f"Частное= {round(private, 2)}")
# мини-проект "Конвертер валют"
rubles=float(input("Ваша сумма"))
euro_1=float(input("Введите текущий курс евро")) #Сам курс на данный момент
euro_2=rubles/euro_1 #Сколько выйдет евро
print(f"{round(rubles, 2)} рублей по курсу {round(euro_1, 2)} - это {round(euro_2, 2)} евро")
# мини-проект "Калькулятор чаевых"
amount_1=float(input("Сумма счета?"))
tips_1=int(input("Процент чаевых?"))
tips_2=tips_1/100*amount_1 #Размер чаевых
amount_2=amount_1+tips_2 #Итоговая сумма
print(f"Итоговая сумма к оплате: {round(amount_2, 2)}")