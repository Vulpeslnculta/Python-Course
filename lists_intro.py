# computer_parts = ["computer",
#                   "monitor",
#                   "keyboard",
#                   "mouse",
#                   "mouse mat"
#                   ]
# for part in computer_parts:
#     print(part)
#
# print("_"*80)
# print(computer_parts[0:3])
# print(computer_parts[-1])

#immutables
#
# result = True
# another_result = result
# print(id(result))
# print(id(another_result))
#
# result = False
# print(id(result))

# result = "Correct"
# another_result = result
# print(id(result))
# print(id(another_result))
#
# result += "ish"
# print(id(result))

# Mutables

shopping_list = ["milk",
                 "pasta",
                 "eggs",
                 "spam",
                 "bread",
                 "rice"
                 ]
another_list = shopping_list
print(id(shopping_list))
print(id(another_list))
shopping_list += ["cookies"]
print(shopping_list)
print(id(shopping_list))
print(another_list)

a=c=b=d=e=f=g=another_list

print(a)
print()
z = input("Add your item of choice:\n")
print("Adding {}".format(z))
b.append(z)
print(c)
print(d)