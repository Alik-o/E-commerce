class Category:
    name: str
    description: str
    __products: list
    _category_count: int
    _product_count: int

    _category_count = 0
    _product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category._category_count += 1
        Category._product_count += len(self.__products)

    def add_product(self, product):
        self.__products.append(product)
        self._product_count += 1

    @property
    def products(self):
        products = ""
        for product in self.__products:
            products += f"{product.name}, {product.price} руб. Остаток: {product.quantity}\n"
        return products

    @classmethod
    def get_category_count(cls):
        return cls._category_count

    @classmethod
    def get_product_count(cls):
        return cls._product_count
