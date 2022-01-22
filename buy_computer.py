available_parts = ["Computer",
                   "Monitor",
                   "Keyboard",
                   "Mouse",
                   "Mouse mat",
                   "Microphone",
                   "DVD drive"
                   ]
valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
print(valid_choices)
current_basket = "-"
computer_parts = []  # empty list
while current_basket != '0':
        if current_basket in valid_choices:
            print("Adding part no. {}".format(current_basket))
            if current_basket == '1':
                computer_parts.append("Computer ")
            elif current_basket == '2':
                computer_parts.append("Monitor ")
            elif current_basket == '3':
                computer_parts.append("Keyboard ")
            elif current_basket == '4':
                computer_parts.append("Mouse ")
            elif current_basket == '5':
                computer_parts.append("Mouse mat ")
            elif current_basket == '6':
                computer_parts.append("Microphone ")
            elif current_basket == '.':
                print(computer_parts)
        else:
            print("Add options from the list below:")
            for number, part in enumerate(available_parts):
                print("{}: {}".format(number + 1, part))
        current_basket = input()
print(computer_parts)