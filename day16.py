numbers=[5, 2, 9]
print("Исходный:", numbers)
numbers.append(7)
print("После append(7):", numbers)
numbers.remove(2)
print("После remove(2):", numbers)
numbers.sort()
print("После sort():", numbers)
last=numbers.pop()
print("Удалили и вернули:", last)
print("Осталось:", numbers)
print("Есть ли 9 в списке?", 9 in numbers)
print("Сумма, максимум, минимум:", sum(numbers), max(numbers), min(numbers))

grades=[4, 5, 3, 4, 2, 5]
average=sum(grades)/len(grades)
best=max(grades)
count=0
for grade in grades:
    if grade>average:
        count+=1
print("Среднее:", average, "Максимум:", best, "Выше среднего:", count)