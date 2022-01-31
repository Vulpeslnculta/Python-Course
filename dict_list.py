available_parts = {"1": "computer",
                   "2": "monitor",
                   "3": "keyboard",
                   "4": "mouse",
                   "5": "hdmi cable",
                   "6": "dvd drive",
                    }

chosen_parts = []
current_choice = None
while current_choice != "0":
    current_choice = input("> ")
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        print(f"Adding {chosen_part}")
        chosen_parts.append(chosen_part)
    else:
        for key in available_parts:
            print(f"\nPart no. {key}")
            print(key, available_parts[key], sep=" - ")
    print("\n0 - to finish")
print(f"You've chosen: {chosen_parts}")