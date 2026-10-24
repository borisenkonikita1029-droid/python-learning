# Квест: Побег из комнаты
name=input("Введи свое имя")
print(f"Привет, {name}! Ты в комнате с закровищами. Реши 3 простые загадки, чтобы узнать, сколько золота ты заработал!")
print("Сундук 1. Уравнение: X+15=40. Чему равен X?")
answer_1=int(input("40-15="))
print("Сундук 2. Уравнение: Y*4=36. Чему равен Y?")
answer_2=int(input("36/4="))
print("Сундук 3. Уравнение: Z-8=12. Чему равен Z?")
answer_3=int(input("12+8="))
total_gold=(answer_1*10+answer_2*20+answer_3*15)
print(f"Игрок {name}, ты ответил на все вопросы правильно и заработал {total_gold} золотых монет!")
# Таймер обратного отсчета
seconds_1=int(input("Введи любое кол-во секунд"))
day=seconds_1//86400
rem_1=seconds_1%86400
hours=rem_1//3600
rem_2=rem_1%3600
minutes=rem_2//60
seconds_2=rem_2%60
print(f"{seconds_1} секунд - это {day} дней, {hours} часов, {minutes} минут и {seconds_2} секунд")
# размен денег
amount_rubles=int(input("Введите сумму денег которую хотите разменять"))
baills_100=amount_rubles//100
ost_1=amount_rubles%100
baills_50=ost_1//50
ost_2=ost_1%50
coins_20=ost_2//20
ost_3=ost_2%20
coins_5=ost_3//5
ost_4=ost_3%5
coins_1=ost_4
print(f"{amount_rubles} рублей - это: купюр по 100: {baills_100}, купюр по 50: {baills_50}, купюр по 20: {coins_20}, монет по 5: {coins_5}, монет по 1: {coins_1}")