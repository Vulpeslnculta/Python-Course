# for i in range(10):
#     print("i is now {}".format(i))
#     Now let's do it other way
# i = 0
# while i < 10:
#     print("i is now {}".format(i))
#     i += 1 # equal to i = i + 1
#
# Adventure game XD

exits = ["north", "south", "east", "west"]

chosen_exit = ""
while chosen_exit.casefold() not in exits:
    chosen_exit = input("Please choose a direction: \n")
    if chosen_exit.casefold() == "quit":
        print("Game has been terminated!")
        break
if chosen_exit.casefold() in exits:
    print("Aren't you glad you got out of there?")
