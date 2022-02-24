entries = [1, 2, 3, 4, 5]

if entries:
    print('all: {}'.format(all(entries)))
else:
    print(False)
print('any: {}'.format(any(entries)))