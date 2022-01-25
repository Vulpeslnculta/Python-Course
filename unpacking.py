a = b = c = d = e = f = 12
print(c)
print()
x, y, z = 1, 2, 72
print(x)
print(y)
print(z)

print("Unpacking a tuple: \n")

data = 1, 2, 72
x, y, z = data
print(x)
print(y)
print(z)

print("\nUnapcking a list:\n")
data_list = [12, 13, 14]
p,q,r = data_list
print(p)
print(q)
print(r)
print()

for index, character in enumerate("abcdefgh"):
    print(index, character)

#  The same as:

for t in enumerate("abcdefgh"):
    print(t)

index, character = (0, 'a')
print(index, character)