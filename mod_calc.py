answer = 'y'

while answer == 'y':
    list1 = float(input("Введи перше число: "))
    list2 = float(input("Введи друге число: "))
    operator = input("Вібері операцію (+, -, *, /): ")

    if operator == '+':
        result = list1 + list2
    elif operator == '-':
        result = list1 - list2
    elif operator == '*':
        result = list1 * list2
    elif operator == '/':
        if list2 != 0:
            result = list1 / list2
        else:
            result = "Ділення на нуль неможливе"
    else:
        result = "Невідома операція"

    print("Результат:", result)
    answer = input("Хочеш продовжити? (y/n): ")