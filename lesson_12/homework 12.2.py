class Item:
    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f"{self.name}, price: {self.price}"


class User:
    def __init__(self, surname, name, patronymic, phone):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.phone = phone

    def __str__(self):
        full_name = f"{self.name} {self.surname}"
        if self.patronymic:
            full_name = f"{self.name} {self.patronymic} {self.surname}"
        return full_name


class Purchase:
    def __init__(self, user):
        self.user = user
        self.products = {}

    def add_item(self, item, cnt):
        if cnt <= 0:
            raise ValueError("Количество должно быть больше 0")
        self.products[item] = cnt

    def get_total(self):
        total = 0
        for item, cnt in self.products.items():
            total += item.price * cnt
        return total

    def __str__(self):
        lines = [f"User: {self.user}", "Items:"]
        for item, cnt in self.products.items():
            lines.append(f"{item.name}: {cnt} pcs.")
        return "\n".join(lines)

lemon = Item("lemon", 5, "yellow", "small")
apple = Item("apple", 2, "red", "middle")

print(lemon)

buyer = User("Ivanov", "Ivan", "", "02628162")
print(buyer)

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)

print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 20 pcs.
"""

assert isinstance(cart.user, User) is True, "Екземпляр класу User"
assert cart.get_total() == 60, "Всього 60"
assert cart.get_total() == 60, "Повинно залишатися 60!"

cart.add_item(apple, 10)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 10 pcs.
"""

assert cart.get_total() == 40
