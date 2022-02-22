import sys


def my_range(n: int):
    print('my_range starts')
    start = 0
    while start < n:
        print('my_range is returning {}'.format(start))
        yield start
        start +=1


big_range = my_range(10)
_ = input("line 12")

print(next(big_range))
print("big_range is {} bytes". format(sys.getsizeof(big_range)))

big_list = []
_ = input('line 18')
for val in big_range:
    _ = input('line 20 inside the loop')
    big_list.append(val)

print("big_list is {} bytes".format(sys.getsizeof(big_list)))
print(big_range)
print(big_list)