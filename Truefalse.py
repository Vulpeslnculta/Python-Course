day = input("What day it is?\n")
temperature = int(input("What temperature is today?\n"))
raining = input("Is it raining? True or False:\n")
if raining == "True":
    raining = True
elif raining == "False":
    raining = False
else:
    print("Wrong input")
if day == "Saturday" and temperature > 27 or not raining:
    print("Go swimming")
else:
    print("Learn python")

