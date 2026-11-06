def add(a,b):
    return a+b
result=add(3,4)
print(result)
print(add(10,5))

def power(base,exponent=2):
    return base**exponent
print(power(5))   #Без второго аргумента (возведет в квадрат)
print(power(2,10))   #С двумя аргументами

def is_even(n):
    return n%2==0
print(is_even(4))

def max_of_two(a,b):
    if a>b:
        return a
    else:
        return b
print(max_of_two(5,9))

def average(numbers):
    return sum(numbers)/len(numbers)
print(average([10,20,30]))

def is_adult(age):
    return age>=18
print(is_adult(20))
print(is_adult(16))
# Проверки для is_adult
assert is_adult(20)==True
assert is_adult(16)==False
assert is_adult(18)==True
# Проверки для max_of_two
assert max_of_two(5,9)==9
assert max_of_two(-1,-5)==-1
# Проверки для average
assert average([10,20,30])==20.0

print("Все проверки пройдены!")