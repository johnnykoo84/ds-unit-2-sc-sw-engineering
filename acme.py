from random import randint


class Product:

    def __init__(self, name, price=10, weight=20, flammability=0.5):
        self.identifier = randint(1000000, 9999999)
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
