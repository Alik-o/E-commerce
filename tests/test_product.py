from src.product import Product


def test_product_init(products):
    assert products.name == "Samsung Galaxy S23 Ultra"
    assert products.description == "256GB, Серый цвет, 200MP камера"
    assert products.price == 180000.0
    assert products.quantity == 5


def test_product_new_product():
    data = {"name": "Product 1", "description": "Description 1", "price": 100.0, "quantity": 10}
    product = Product.new_product(data)
    assert product.name == "Product 1"
    assert product.description == "Description 1"
    assert product.price == 100.0
    assert product.quantity == 10


def test_product_price(products):
    products.price = 800
    assert products.price == 800
    products.price = -100
    assert products.price == 800
    products.price = 0
    assert products.price == 800


def test_product_str(products):
    assert str(products) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5\n"


def test_product_add(products, products_1):
    assert products + products_1 == 2580000.0
