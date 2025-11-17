nums = [0, 1, 7, 2, 4, 8]
total = 0

if nums == []:
    result = 0
else:
    total = 0
    for n in range(0, len(nums), 2):
        total += nums[n]
    result = total * nums[-1]
print(result)