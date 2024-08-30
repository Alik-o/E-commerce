from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity, color=None):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.color = color
        super().__init__()

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity}\n"

    def __add__(self, other):
        return self.price * self.quantity + other.price * other.quantity

    @classmethod
    def new_product(cls, data):
        return cls(**data)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не может быть меньше или равна нулю")
        else:
            self.__price = value
