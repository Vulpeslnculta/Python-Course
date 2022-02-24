import timeit

burgers = ['beef', 'chicken', 'tofu']
toppings = ['cheese', 'egg', 'beans', 'beacon']

for meals in [(burger, topping) for burger in burgers for topping in toppings]:
    print(meals)


nested_comp = """\
for numbers in [(i, i * j) for i in range(1,11) for j in range(1, 11)]:
    print(numbers)
"""
timing_result = timeit.timeit(nested_comp, number=10000)
print("Nested comp:\t{}".format(timing_result))