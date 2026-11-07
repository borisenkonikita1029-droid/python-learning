numbers=[5, 10, 15]
def get_doubled(numbers_list):
    result=[]
    for number in numbers_list:
        result.append(number*2)
    return result
print(get_doubled(numbers))

phones = [
    {"model": "iPhone 13", "price": 800},
    {"model": "Samsung S22", "price": 700},
    {"model": "Xiaomi Redmi", "price": 300},
    {"model": "Google Pixel", "price": 600}
]
def find_expensive_phones(phones_list, max_price):
    expensive_models = []
    for phone in phones_list:
        if phone["price"]>max_price:
            expensive_models.append(phone["model"])
    return expensive_models
print(find_expensive_phones(phones, 500))