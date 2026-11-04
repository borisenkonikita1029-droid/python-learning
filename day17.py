person={"name": "Анна", "age": 20, "city": "Париж"}
print(person["name"])   #Анна
person["age"]=21    #Изменили возраст
person["job"]="студентка"   # Добавили новую пару
print("city" in person)
print(person.get("phone", "нет данных"))    # Безопасный поиск
for key, value in person.items():
    print(f"{key}: {value}")

contacts={"Олег": "345-961", "Никита": "312-745", "Саша": "421-934"}
name=input("Какой контакт вы хотите найти?")
print(contacts.get(name, "Контакт не найден"))
print(contacts)