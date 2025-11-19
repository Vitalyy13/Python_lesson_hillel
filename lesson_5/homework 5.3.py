import string

text = input("Введите строку: ").strip()
clean_text = ""


for ch in text:
    if ch in string.punctuation:
        clean_text += " "
    else:
        clean_text += ch
words = clean_text.split()
capitalized_words = []
for word in words:
    new_word = word.capitalize()
    capitalized_words.append(new_word)
result = "".join(capitalized_words)
hashtag = "#" + result
if len(hashtag) > 140:
    hashtag = hashtag[:140]
print(hashtag)






















