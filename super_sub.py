animals = {'Turtle',
           'Horse',
           'Robin',
           'Python',
           'Swallow',
           'Hedgehog',
           'Wren',
           'Aardvark',
           'Cat',
           }
birds = {'Robin', 'Swallow', 'Wren'}

print(f"birds is a subset of animals {birds.issubset(animals)}")
print(f"animals is superset of birds {animals.issuperset(birds)}")

print(f"birds is a superset of animals {birds.issuperset(animals)}")

print(birds <= animals)
print(birds <= animals)

print("_" * 80)

garden_birds = {'Swallow', 'Wren', 'Robin'}

print(birds == garden_birds)
print(garden_birds <= birds)
print(garden_birds < birds)

print("_" * 80)

more_birds = {'Wren', 'Budgie', 'Swallow'}
print(garden_birds >= more_birds)