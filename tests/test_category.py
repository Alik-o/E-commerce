from src.category import Category
from src.product import Product


def test_category_init(category, category_2):
    assert category.name == "Смартфоны"
    assert (
        category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert category_2.name == "Телевизоры"
    assert (
        category_2.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert category.product_count == 3
    assert category.category_count == 2


def test_category_products(category):
    assert category.products == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5\n" "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14\n"
    )


def test_category_add_product(category):
    product = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category.add_product(product)
    assert category.product_count == 8


def test_category_str(products):
    category = Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни",
        products=[products, Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)],
    )

    assert str(category) == "Смартфоны, количество продуктов: 19\n"
