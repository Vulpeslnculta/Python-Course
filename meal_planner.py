from contents import pantry, recipes

#  should use comprehension here

display_dict = {}
shopping_list = {}
for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key

while True:
    print("Pick your meat and eat !")
    print("________________________")
    for key, value in display_dict.items():
        print(f"{key} - {value}")

    choice = input(": ")

    if choice == "0":
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"Your meat to eat is: {selected_item}, ENJOY!")
        print("Checking if ingredients are here ... ")
        ingredients = recipes[selected_item]
        for food_item, required_quantity in ingredients.items():
            quantity_in_pantry = pantry.get(food_item, 0)
            buy_quantity = required_quantity - quantity_in_pantry
            if required_quantity <= quantity_in_pantry:
                print(f"'\t{food_item} is here")
            else:
                print(f"\tSorry you are missing: {food_item} in quantity {buy_quantity}")
                shopping_list[food_item] = buy_quantity
        print(f"Your shopping list includes:\n\t{shopping_list}\n\n")