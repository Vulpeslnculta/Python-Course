List = ["Milk", "Pasta", "Eggs", "Spam", "Bread", "Rice"]
# for item in shopping_list:
#     if item == "Spam":
#         break
#
#     print("Buy " + item)

item_to_find = input("What data you want to find? :\n")
found_at = None

# for index in range(len(List)):
#     if List[index] == item_to_find:
#         found_at = index
#         break

if item_to_find in List:
    found_at = List.index(item_to_find)

if found_at is not None:
    print("Item found on position {}".format(found_at))
else:
    print("There is no such item as {} on a list, or you did a typo".format(item_to_find))