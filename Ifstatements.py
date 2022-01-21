name = input("Please enter your name: \n")
age = int(input("How old are you, {0} ?\n".format(name)))
print(age)
print(type(age))
print()
if age >= 18:
    input("Choose your candidate for Presidential council: \n")
else:
    print("You are too young to vote!")
    print("Please come back in {0} years".format(18-age))
