print(__file__)

numbers = [1, 2, 3, 4, 5, 6]

# squares = [number ** 2 for number in numbers]
n = int(input("Please enter the max number in a string of squares: \n"))
squares = [number ** 2 for number in range(1, n + 1)]

print(squares)