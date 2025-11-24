
number = int(input("Введіть число: "))
seconds_in_day = 86400
days, rest = divmod(number, seconds_in_day)
h, m = divmod(rest, 3600)
m, s = divmod(m, 60)
h_str = str(h).zfill(2)
m_str = str(m).zfill(2)
s_str = str(s).zfill(2)
last_two = days % 100
last_digit = days % 10
if last_digit == 1 and last_two != 11:
    day_word = "день"
elif last_digit in (2, 3, 4) and last_two not in (12, 13, 14):
    day_word = "дні"
else:
    day_word = "днів"
print(f"{days} {day_word}, {h_str}:{m_str}:{s_str}")
