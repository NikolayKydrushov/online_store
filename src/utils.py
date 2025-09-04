import json
import os

from dotenv import load_dotenv

from src.main import Category, Product

load_dotenv("../.env")

PATH_FILE = os.getenv("PATH_FILE")
# PATH_FILE = 'C:/Skypro/online_store/data/products.json'


def reader_products(file_path: str) -> list:

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            # return data
    except json.JSONDecodeError:
        return []
    except FileNotFoundError:
        return []
    except TypeError:
        return []
    except ValueError:
        return []

    category_1 = Category(data[0]["name"], data[0]["description"], data[0]["products"])

    prod_1_1 = Product(
        data[0]["products"][0]["name"],
        data[0]["products"][0]["description"],
        data[0]["products"][0]["price"],
        data[0]["products"][0]["quantity"],
    )

    prod_1_2 = Product(
        data[0]["products"][1]["name"],
        data[0]["products"][1]["description"],
        data[0]["products"][1]["price"],
        data[0]["products"][1]["quantity"],
    )

    prod_1_3 = Product(
        data[0]["products"][2]["name"],
        data[0]["products"][2]["description"],
        data[0]["products"][2]["price"],
        data[0]["products"][2]["quantity"],
    )

    category_2 = Category(data[1]["name"], data[1]["description"], data[1]["products"])

    prod_2_1 = Product(
        data[1]["products"][0]["name"],
        data[1]["products"][0]["description"],
        data[1]["products"][0]["price"],
        data[1]["products"][0]["quantity"],
    )

    categories = {category_1: [prod_1_1, prod_1_2, prod_1_3], category_2: [prod_2_1]}
    return categories


data_from_products = reader_products(PATH_FILE)
print(data_from_products)
