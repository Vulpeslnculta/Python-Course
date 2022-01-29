BLACK = "\u001b[30m"
RED = '\u001b[31m'
GREEN = "\u001b[32m"
YELLOW = "\u001b[33m"
BLUE = "\u001b[34m"
MAGENTA = "\u001b[35m"
CYAN = "\u001b[36m"
WHITE = "\u001b[37m"
RESET = "\u001b[0m"

BOLD = "\u001b[1m"
UNDERLINE = "\u001b[4m"
REVERSE = "\u001b[7m"


def colour_print(text: str, *effects: str) -> None:

    '''
    Print `text` using the ANSI sequences to change colour, etc.

        :param text: The text to print.
        :param effects: The effect(s) we want. One or more of the constants defined at the start.
    '''
    effect_string = "".join(effects)
    output_string = "{}{}{}".format(effect_string, text, RESET)
    print(output_string)


colour_print("Hello, Red", RED, BOLD, UNDERLINE)
colour_print("Hello, Blue", BLUE)
print("Default terminal colour")
colour_print("Hello, Magenta", MAGENTA, REVERSE)
colour_print("UNDERLINED", UNDERLINE)