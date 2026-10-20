#это коментарий, который Python читать не может
name="Анна"
age=20
print(name)
print(age)
age=21
print(age)

city="Шклов"
color="красный"
number=33
print(city)
print(color)
print(number)
print("city")
print(city)

#доп практика: обмен значений
a=1
b=2
print("до обмена:", a,b)
tmp=a #Кладем значение а во временную коробку tmp
a=b #Кладем значение b в a
b=tmp #Достаем из tmp старое значение а и кладем в b
print("После обмена:", a,b)