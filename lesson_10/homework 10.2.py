def normalize_text(func):
    """Нормалізує рядок: прибирає крапки, коми та зайві пробіли."""
    def wrapper(text):
        cleaned = text.replace('.', ' ').replace(',', ' ')
        cleaned = cleaned.strip()
        cleaned = ' '.join(cleaned.split())
        return func(cleaned)
    return wrapper


@normalize_text
def first_word(text):
    """Пошук першого слова в рядку."""
    words = text.split()
    return words[0]

assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')
