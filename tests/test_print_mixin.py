from src.product import Product


def test_print_mixin(capsys):
    Product("Samsung Galaxy S23 Ultra", "256GB, Серий цвет, 200MP камера", 180000.0, 5)
    message = capsys.readouterr()
    assert message.out.strip() == ("Product(Samsung Galaxy S23 Ultra, 256GB, Серий цвет, 200MP камера, 180000.0, 5)")
