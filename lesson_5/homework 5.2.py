answer = ("y")
while answer == ("y") or answer == ("yes"):
    number = float(input("Введите первое число: "))
    operation = input("Введите операцию +, -, *, /: ")
    number_2 = float(input("Введите второе число: "))

    if operation == "+":
        result = number + number_2
        print(f"Результат: {result:.2f}")
    elif operation == "-":
        result = number - number_2
        print(f"Результат: {result:.2f}")
    elif operation == "*":
        result = number * number_2
        print(f"Результат: {result:.2f}")
    elif operation == "/":
        if number_2 == 0:
            print("Ділити на нуль не можна")
        else:
            result = number / number_2
            print(f"Результат: {result:.2f}")
    else:
        print("Невідома операція")
    answer = input("Хочете продовжити? (y/yes): ").strip().lower()
else:
    print("Завершення роботи.")