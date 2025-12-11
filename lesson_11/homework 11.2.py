def generate_cube_numbers(end):
    """
    Генератор кубів чисел, починаючи з 2,
    який видає куби, поки cube <= end.
    """
    num = 2
    while True:
        cube = num ** 3
        if cube > end:
            return
        yield cube
        num += 1


from inspect import isgenerator

gen = generate_cube_numbers(1)
assert isgenerator(gen) == True, 'Test0'
assert list(generate_cube_numbers(10)) == [8]
assert list(generate_cube_numbers(100)) == [8, 27, 64]
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000]
