#!/usr/bin/env python

from random import randint, sample, uniform, choice
import numpy as np
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    # TODO - your code! Generate and add random products.
    for i in range(num_products):
        name = f"{choice(ADJECTIVES)} {choice(NOUNS)}"
        products.append(name)
    return products


def inventory_report(products):
    # pass  # TODO - your code! Loop over the products to calculate the report.
    products_objs = []
    for name_product in products:
        price = randint(5, 10)
        weight = randint(5, 10)
        flammability = uniform(0, 2.5)
        product_obj = Product(name_product, price, weight, flammability)
        products_objs.append(product_obj)
    uniq_names = np.unique(products)
    price_mean = np.mean([p.price for p in products_objs])
    weight_mean = np.mean([p.weight for p in products_objs])
    flamm_mean = np.mean([p.flammability for p in products_objs])
    print('ACME CORPORATION OFFICIAL INVENTORY REPORT\n')
    print(f"Unique product names: {len(uniq_names)}")
    print(f"Average price: {price_mean}")
    print(f"Average weight: {weight_mean}")
    print(f"Average flammability: {flamm_mean}")


if __name__ == '__main__':
    inventory_report(generate_products())
