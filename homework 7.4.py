def common_elements():
    multiples_of_3 = [x for x in range(100) if x % 3 == 0]
    multiples_of_5 = [x for x in range(100) if x % 5 == 0]
    set_3 = set(multiples_of_3)
    set_5 = set(multiples_of_5)
    common = set_3.intersection(set_5)
    return common
assert common_elements() == {0, 15, 30, 45, 60, 75, 90}, 'Test1'
print('ОК')

