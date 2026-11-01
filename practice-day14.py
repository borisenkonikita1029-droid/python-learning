secret=10
win=False
attempts=3
for i in range(3):
    attempts=attempts-1
    number=int(input("Введите число"))
    if number==secret:
        print(f"Вы угадали за {3-attempts} {'попытку' if (3-attempts)==1 else 'попытки'}, победа!")
        win=True
        break
    if number>secret:
        print(f"Загаданное число меньше, осталось {attempts} {'попытка' if attempts==1 else 'попытки'}")
    if number<secret:
        print(f"Загаданное число больше, осталось {attempts} {'попытка' if attempts==1 else 'попытки'}")   
if win==False:
    print("Попытки закончились, загаданное число было 10")