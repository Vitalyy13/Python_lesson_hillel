# number = int(input("Введіть 4-х значне число: "))
# digit1 = number // 1000
# digit2 = (number // 100) % 10
# digit3 = (number // 10) % 10
# digit4 = number % 10

# print(digit1)
# print(digit2)
# print(digit3)
# print(digit4)

# x = int(input("Введіть число: "))
# y = x ** 2
# print(y)

# x = int(input("Введіть число: "))
# y = int(input("Введіть число: "))
# a = int(input("Введіть число: "))
#
# b = (x + y + a) / 3
# print(b)

text = int(input("Введіть 4-х значне число: "))
d1, rest = divmod(text, 1000)
d2, rest = divmod(rest, 100)
d3, rest = divmod(rest, 10)
d4, rest = divmod(rest, 1)
print(d1)
print(d2)
print(d3)
print(d4)