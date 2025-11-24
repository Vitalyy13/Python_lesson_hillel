number = int(input("Введіть число: "))

while number > 9:
    product = 1
    for ch in str(number):
        product *= int(ch)
    number = product
print(number)
