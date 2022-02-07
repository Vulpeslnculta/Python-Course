def python_food():
    width = 80
    text = 'spam and eggs'
    left_margin = (width - len(text)) // 2
    print(' ' * left_margin, text)


def centre_text(*args, sep=" "):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    return ' ' * left_margin, text


# with open('centered', mode='w') as centred_file:
# s1 = centre_text("This text is centered")
# print(s1)
# s2 = centre_text("And that too")
# print(s2)
# s3 = centre_text(12)
# print(s3)
# s4 = centre_text("blah", "blah", "gibberish", 12, 'blah')
# print(s4)
# print()
# print('_'*80)
# print(sorted(['b', 'd', 'c', 'a']))

with open('menu', 'w') as menu:
    s1 = centre_text("This text is centered")
    print(s1, file=menu)
    s2 = centre_text("And that too")
    print(s2, file=menu)
    s3 = centre_text(12)
    print(s3, file=menu)
    s4 = centre_text("blah", "blah", "gibberish", 12, 'blah')
    print(s4, file=menu)