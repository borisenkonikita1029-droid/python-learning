numbers=[4, 8, 15, 16, 23, 42]
count=0
total=0
for number in numbers:
    if number%2==0:
        count+=1
        total+=number
print("Кол-во четных:", count, "Сумма четных:", total)

temps=[12, 25, -3, 18, 30, 15, -5]
warm_days=0
sum_days=0
for temp in temps:
    if temp>15:
        warm_days+=1
        sum_days+=temp
print("Теплых дней:", warm_days, "Сумма температур:", sum_days)

backpack=["палатка", "спальник", "фонарик"]
backpack.append("котелок")
backpack.append("аптечка")
backpack.remove("фонарик")
backpack.sort()
print("Аптечка в рюкзаке:", "аптечка" in backpack)
print(backpack)