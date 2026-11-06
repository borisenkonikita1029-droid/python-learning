products=[
    {"name": "Хлеб", "price": 40},
    {"name": "Молоко", "price": 80},
    {"name": "Сыр", "price": 200},
    {"name": "Яблоки", "price": 60},
]
def find_cheap(products_list, max_price):
    cheap_names=[]
    for product in products_list:
        if product["price"]<=max_price:
            cheap_names.append(product["name"])
    return cheap_names
print(find_cheap(products, 100))

cars=[
    {"brand": "Toyota", "year": 2015},
    {"brand": "BMW", "year": 2008},
    {"brand": "Audi", "year": 2020},
    {"brand": "Ford", "year": 2010}
]
def find_old_cars(cars_list, min_year):
    old_brands=[]
    for car in cars_list:
        if car["year"]<=min_year:
            old_brands.append(car["brand"])
    return old_brands
print(find_old_cars(cars,2012))

grades = [
    {"subject": "Математика", "grade": 4},
    {"subject": "История", "grade": 5},
    {"subject": "Физика", "grade": 3},
    {"subject": "Химия", "grade": 5},
    {"subject": "Литература", "grade": 2}
]
def get_average_for_subject(grades_list, target_grade):
    matching_grades=[]
    matching_subject=[]
    for g in grades_list:
        if g["grade"]==target_grade:
            matching_grades.append(g["grade"])
            matching_subject.append(g["subject"])
    average=sum(matching_grades)/len(matching_grades)
    return matching_subject, average
print(get_average_for_subject(grades, 5))