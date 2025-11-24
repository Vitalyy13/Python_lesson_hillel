import string

text = input("Введите текст: ").strip()
tex = text.split("-")
letters = string.ascii_letters

start_char = tex[0]
end_char = tex[1]
pos_1 = letters.find(start_char)
pos_2 = letters.find(end_char)
result = letters[pos_1:pos_2+1]
print(result)