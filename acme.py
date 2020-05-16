from random import randint


class Product:

    def __init__(self, name, price=10, weight=20, flammability=0.5):
        self.identifier = randint(1000000, 9999999)
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability

    def stealability(self):
        result = self.price / self.weight
        if result < 0.5:
            message = 'Not so stealable...'
        elif (result >= 0.5) & (result < 1):
            message = 'Kinda stealable.'
        else:
            message = 'Very stealable!'
        return message

    def explode(self):
        result = self.flammability * self.weight
        if result < 10:
            message = '...fizzle.'
        elif (result >= 10) & (result < 50):
            message = '...boom!'
        else:
            message = '...BABOOM!!'
        return message
