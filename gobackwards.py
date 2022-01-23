data =[104, 111, 4, 105, 345, 132, 53, 645, 24, 145, 190]
min_valid = 100
max_valid = 250

# for index in range(len(data) - 1, - 1, - 1):
#     if data[index] < min_valid or data[index] > max_valid:
#         print(index, data)
#         del data[index]
top_index = len(data) - 1
for index, value in enumerate(reversed(data)):
    if value < min_valid or value > max_valid:
        print(top_index - index, value)
        del data[top_index - index]

print(data)
