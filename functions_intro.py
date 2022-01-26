def multiply(x, y):
    result = x * y
    return result


def is_palindrome(string):
    return string[::-1].casefold() == string.casefold()


# answer = multiply(int(input()), int(input()))
# print(answer)

print()

# for val in range(1, 5):
#     two_times = multiply(2, val)
#     print(two_times)

word = input("Please enter a word or a sentence to check: \n")
if is_palindrome(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a palindrome".format(word))
