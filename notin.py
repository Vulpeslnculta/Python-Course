activity = input("What would you like to do today?\n")

if "cinema" not in activity.casefold():
    print("But I want to go to the cinema!")
else:
    print("Yey!")