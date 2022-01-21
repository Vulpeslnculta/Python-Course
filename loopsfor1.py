parrot = "Norwegian Blue "

for character in parrot:
    print(character)

pi = str(421535//5)
for digit in pi:
    print(digit)

number = input("Please enter a number: \n")
separators = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char

print("that's your separators: " + separators)
values = "".join(char if char not in separators else " " for char in number).split()
print(sum([int(val) for val in values]))
