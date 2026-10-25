# Сложный процент (депозит в банке)
amount_1=float(input("Введите начальную сумму вклада"))
rate=float(input("Введите процентную ставку"))
years=int(input("На какое кол-во лет?"))
amount_2=amount_1*(1+rate/100)**years
profit=amount_2-amount_1
print(f"Через {years} лет на счету будет: {round(amount_2, 2)} рублей")
print(f"Чистая прибыль: {round(profit, 2)} рублей")