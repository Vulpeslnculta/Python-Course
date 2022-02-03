numbers = {}
numbers2 = {*""}
numbers3 = {*{}}
numbers4 = set()

print(numbers, type(numbers))
print(numbers2, type(numbers2))
print(numbers3, type(numbers3))
print(numbers4, type(numbers4))

while len(numbers2) < 4:
    next_value = int(input("Please enter tour next value: \n"))
    numbers2.add(next_value)
print(numbers2)

listed = list("to be or not to be")
listed = set(listed)
print(listed)

data = ["blue", "red", "blue", "green", "red", "blue", "white"]

unique_data = sorted(set(data))
print(unique_data)

unique_data = list(dict.fromkeys(data))
print(unique_data)