import random

length = random.randint(3, 10)
numbers = []

for n in range(length):
    numbers.append(random.randint(1, 10))
new_list = [numbers [0]] + [numbers [2]] + [numbers [-2]]

print("Початковий список:", numbers)
print("Новий список:", new_list)