available_parts = {"1": "computer",
                   "2": "monitor",
                   "3": "keyboard",
                   "4": "mouse",
                   "5": "hdmi cable",
                   "6": "dvd drive",
                    }

current_choice = None
computer_parts = {}

while current_choice != "0":
    current_choice = input("> ")
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        if current_choice in computer_parts:
            print(f"Removing {chosen_part}")
            computer_parts.pop(current_choice)
        else:
            print(f"Adding to cart: {chosen_part}")
            computer_parts[current_choice] = chosen_part
        print(f"Your cart now contains: {computer_parts}")
    else:
        for key in available_parts:
            print(f"\nPart no. {key}")
            print(key, available_parts[key], sep=" - ")
        print("\n0 - to finish")
print(f"Congratulations for buying: {computer_parts}\n"
      f"Your order will be dropshipped in 2/3 months :)")