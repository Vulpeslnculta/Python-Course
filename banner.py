def banner_text(text=" ", screen_width=80):
    """
    Formatting text into form of banner.
    
        :param text: Given text to format, line must be shorter than screen_width
        :param screen_width: Defines maximum length of one line of text

        :return: Formatted text in form of banner with asterisks as frame
    """
    if len(text) > screen_width - 4:
        raise ValueError("String {} is larger than specified width {}"
        .format(text, screen_width))

    if text == "*":
        print("*" * screen_width)
    else:
        centered_text = text.center(screen_width - 4)
        output_string = "**{0}**".format(centered_text)
        print(output_string)


screen_width = int(input("Please enter designated width:\n"))
banner_text("*", screen_width)
banner_text("Always look on the bright side of life...", screen_width)
banner_text("If life seems jolly rotten,", screen_width)
banner_text("There's something you've forgotten!", screen_width)
banner_text("And that's to laugh and smile and dance and sing,", screen_width)
banner_text()
banner_text("When you're feeling in dumps,", screen_width)
banner_text("Don't be silly chumps,", screen_width)
banner_text("Just purse your lips and whistle- that's the thing!", screen_width)
banner_text("And... always look on the bright side of life...", screen_width)
banner_text("*", screen_width)