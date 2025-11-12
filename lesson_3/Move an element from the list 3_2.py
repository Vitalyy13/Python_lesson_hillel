
lst = [12, 3, 4, 10, 13]

if len(lst) <= 1:
    print(lst)
else:
    last = lst.pop()
    lst.insert(0, last)
    print(lst)
