import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def products():
    return Product(
        name="Samsung Galaxy S23 Ultra", description="256GB, Серый цвет, 200MP камера", price=180000.0, quantity=5
    )

@pytest.fixture
def products_1():
    return Product(
        name="Iphone 15, description=", description="512GB, Gray space", price=210000.0, quantity=8
    )

@pytest.fixture
def category(products):
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни",
        products=[products, Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)],
    )


@pytest.fixture
def category_2():
    return Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет наслаждаться просмотром, "
        "станет вашим другом и помощником",
        products=[Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)],
    )
