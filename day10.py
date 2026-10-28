age=10
has_ticket=True
print(age>=18 and has_ticket)   # True (и возраст, и билет есть)
print(age<12 or age>65)   # False (20 не подходит ни под одно)
print(not has_ticket)   # False (Потому что билет ЕСТЬ)

age=int(input("Введите свой возраст"))
if age>=6 and age <=17:
    print("Детский билет: 5 рублей")
elif age>=18 and age<=64:
    print("Взрослый билет: 10 рублей")
else:
    print("Билет бесплатный")

years=int(input("Введите год"))
if (years%4 == 0 and years%100!=0) or (years%400==0):
    print("Год високосный")
else:
    print("Год не високосный")