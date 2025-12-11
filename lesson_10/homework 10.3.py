def to_bool_even(func):
    """Декоратор: перетворює результат func(digit) у True/False для парності"""
    def wrapper(digit):
        result = func(digit)
        return result == 0
    return wrapper


@to_bool_even
def is_even(digit):
    """ Перевірка чи є парним число """
    return digit % 2

assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
print('OK')
