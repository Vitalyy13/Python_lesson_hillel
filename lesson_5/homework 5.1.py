import string
import keyword

name = input("Введите имя: ").strip()


if name == "":
    print(False)
elif name[0].isdigit():
    print(False)
elif keyword.iskeyword(name):
    print(False)
elif " " in name:
    print(False)
else:
    allowed = string.ascii_lowercase + string.digits + "_"
    is_ok = True
    for ch in name:
        if ch not in allowed:
            is_ok = False
            break
    if is_ok and len(name) > 1 and all(ch == "_" for ch in name):
        is_ok = False
    print(is_ok)















