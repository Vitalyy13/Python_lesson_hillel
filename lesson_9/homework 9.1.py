def popular_words (text, words):
    text_words = text.lower().split()
    result = {}
    for w in words:
        count = text_words.count(w)
        result[w] = count
    return result
print(popular_words(
    '''When I was One I had just begun When I was Two I was nearly new ''',
    ['i', 'was', 'three', 'near']
))
assert popular_words(
    '''When I was One I had just begun
       When I was Two I was nearly new''',
    ['i', 'was', 'three', 'near']
) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}
print('OK')
