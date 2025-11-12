lst = [1, 2, 3, 4, 5, 6]

if not lst:
    res = [[], []]
    print(res)
else:
    middle = (len(lst) + 1) // 2
    res = [lst[:middle], lst[middle:]]
    print(res)