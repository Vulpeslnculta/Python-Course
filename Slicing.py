parrot = "Norwegian Blue"

print(parrot[0:6])
print(parrot[5:8])
print(parrot[0:9])
print(parrot[ :9])
print(parrot[10:])
print(parrot[ :6])
print(parrot[6: ])

print(parrot[ :6] + parrot[6: ])

print()

abc = "abcdefghijklmnopqrstuvwxyz"

print(abc[7])
print(abc[4])
print(abc[11])
print(abc[11])
print(abc[14])
print()
print(abc[-4])
print(abc[14])
print(abc[17])
print(abc[11])
print(abc[3])

print()

print(abc[3:18:2])
print()
number = "9,223,372,036,854,775,807"
print(number[1::4])
separators = number[1::4]

# backward slicing
print()

backwards = abc[25::-1]
print(backwards)

