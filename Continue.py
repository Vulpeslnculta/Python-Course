shopping_list = ["Milk", "Pasta", "Eggs", "Spam", "Bread", "Rice"]

# for item in shopping_list:
#     if item != "Spam":
#         print("Buy " + item)

for item in shopping_list:
    if item == "Spam":
        continue

    print("Buy " + item)