parrot = "Norwegian Blue"
letter = input("Enter a character: \n")

if letter in parrot.casefold():
    print ("{} is in {}".format(letter, parrot))
else:
    print("I don't need that letter")