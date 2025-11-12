number = float(input("Введіть число: "))
number_1 = float(input("Введіть число: "))
operation = input("Введіть дію (+, -, *, /): ")


if operation == "+":
    result = number + number_1
    print(f"{number} {operation} {number_1} = {result}")
elif operation == "-":
    result = number - number_1
    print(f"{number} {operation} {number_1} = {result}")
elif operation == "*":
    result = number * number_1
    print(f"{number} {operation} {number_1} = {result}")
elif operation == "/":
    if number_1 == 0:
        print("Ділити на нуль не можна")
    else:
        result = number / number_1
        print(f"{number} {operation} {number_1} = {result}")
else:
    print("Невідома дія")
