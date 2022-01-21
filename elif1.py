name = input("Please enter your name: \n")
age = int(input("How old are you, {0} ?\n".format(name)))
print(age)
print(type(age))
print()
if age < 18:
    print("You are too young to vote!")
    print("Please come back in {0} years".format(18-age))
elif age > 850 + age < 950:
    print("Sorry Yoda, you die in the Return of the Jedi :((")
else:
    input("Choose your candidate for Presidential council: \n")

