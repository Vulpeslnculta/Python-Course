value = input("Please enter three numbers: \n")
values = value.replace(",", " ")
x = values.split()
for index in range(len(x)):
    x[index] = int(x[index])
a, b, c = x
d = a + b - c
print(d)