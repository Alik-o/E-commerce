from src.product import Product


class Category:
    name: str
    description: str
    __products: list
    category_count: int
    product_count: int

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __str__(self):
        quantity = 0
        for product in self.__products:
            quantity += product.quantity

        return f"{self.name}, количество продуктов: {quantity}\n"

    def add_product(self, product):
        if isinstance(product, Product):
            self.__products.append(product)
            self.product_count += 1
        else:
            raise TypeError

    @property
    def products(self):
        products = ""
        for product in self.__products:
            products += str(product)
        return products

    def middle_price(self):
        try:
            return round(sum([product.price for product in self.__products]) / len(self.__products), 2)
        except ZeroDivisionError:
            return 0
