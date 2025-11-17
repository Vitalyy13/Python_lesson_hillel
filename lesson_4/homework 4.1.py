numbers = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
result = []
zeros = 0

for num in numbers:
    if num != 0:
        result.append(num)
    else:
        zeros += 1
for i in range(zeros):
    result.append(0)
print(result)












































