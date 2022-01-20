string1 = "he's "
string2 = "probably "
string3 = "pining "
string4 = "for the "
string5 = "fjords"

print(string1 + string2 + string3 + string4 + string5)
print("\tHello \n" * 5)


today = "friday"
print("day" in today)
print("fri" in today)
print("thur" in today)

age = input("Please, enter your age : ")
print("My age is " + str(age) + " years")
print("My age is {0} years".format(age))

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}"
      .format(31, "jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))