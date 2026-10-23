x=10
y=3.14
z="текст"
w=True

#Рентген (проверяем типы)
print(type(x))
print(type(y))
print(type(z))
print(type(w))

#магия разных типов
print("5"+"5") #Склеивание текста
print(5+5) #сложение чисел
print(int("5")+5) #Превращение текста в число и сложение

number_str="42"
number_int_2=8
print(int(number_str)+number_int_2)

#проверка типов
print(type(3.9))
print(type("3.9"))
print(type(True))
print(type(3))

#Преобразование типов
print(int(3.9)) #что будет с дробью?
print(float(2)) #что будет с целым?
print(str(100)+"руб") #Что будет с числом и текстом