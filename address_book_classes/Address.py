class Address:
    def __init__(self, text):
        if not text:
            raise ValueError("Будь ласка, уведіть текст у текстовому форматі.")
        if not any(char.isalpha() for char in text):
            raise ValueError("Текст повинен містити принаймні одину літеру.")
        self.text = text

    def __str__(self):
        return self.text

# приклади використання
try:
    address1 = Address("Кучеренка 8, Полтава")
    print(address1)
except ValueError as e:
    print(e)

try:
    address2 = Address("36009")
    print(address2)
except ValueError as e:
    print(e)

try:
    address3 = Address("")
    print(address3)
except ValueError as e:
    print(e)
