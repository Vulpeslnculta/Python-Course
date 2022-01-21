name = input("What's your name?\n")
age = int(input("Hello! May I ask, how old are you, {}?\n".format(name)))


if age > 30 or age < 17:
    print("Sorry {}, but you cannot enter here".format(name))
else:
    print("Allrighty {}, be my guest!".format(name))