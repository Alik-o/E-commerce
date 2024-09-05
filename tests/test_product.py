import pytest

from src.product import Product


def test_product_init(products):
    assert products.name == "Samsung Galaxy S23 Ultra"
    assert products.description == "256GB, Серый цвет, 200MP камера"
    assert products.price == 180000.0
    assert products.quantity == 5


def test_product_new_product(products):
    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.price == 180000.0
    assert new_product.quantity == 5


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


def test_product_quantity_zero():
    with pytest.raises(ValueError):
        Product("Бракованный товар", "Неверное количество", 1000.0, 0)
