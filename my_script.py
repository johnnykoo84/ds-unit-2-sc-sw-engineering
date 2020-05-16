from acme import Product
from acme import BoxingGlove

# part 1, 2
prod = Product('A Cool Toy')

print(prod.name)  # 'A Cool Toy'
print(prod.price)  # 10
print(prod.weight)  # 20
print(prod.flammability)  # 0.5
print(prod.identifier)  # ?

print(prod.stealability())
print(prod.explode())

# part 3
glove = BoxingGlove('Punchy the Third')
print(glove.price)  # 10
print(glove.weight)  # 10
print(glove.punch())  # 'Hey that hurt!'
print(glove.explode())  # "...it's a glove."
