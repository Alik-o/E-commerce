import json
import os

from config import DATA_DIR
from src.category import Category
from src.product import Product


def load_json(path: str) -> list[dict]:
    """Загружает json из файла"""
    with open(os.path.join(DATA_DIR, path), "r", encoding="utf-8") as file:
        return json.load(file)


def create_object_from_json(data: list) -> list:
    """Создает объекты из словаря"""
    result = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(product["name"], product["description"], product["price"], product["quantity"]))
        result.append(Category(category["name"], category["description"], products))

    return result
