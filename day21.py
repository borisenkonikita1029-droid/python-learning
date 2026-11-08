tasks=[]
def show_tasks():
    for i in range(len(tasks)):
        print(f"{i + 1}. {tasks[i]}")
def add_tasks():
    task=input("Введите текст новой задачи")
    tasks.append(task)
def remove_task():
    number_task=int(input("Введите номер задачи которую хотите удалить"))
    tasks.pop(number_task-1)
while True:
    print("1 показать задачи")
    print("2 добавить задачу")
    print("3 удалить задачу")
    print("0 выход")
    action=input("Выберите действие которое хотите совершить").strip()
    if action=="1":
        show_tasks()
    elif action=="2":
        add_tasks()
    elif action=="3":
        remove_task()
    elif action=="0":
        break
    else:
        print("Нет такого действия")