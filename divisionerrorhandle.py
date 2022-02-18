import sys


def getting_int(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Invalid number entered, please try again!")
        except EOFError:
            sys.exit(1)


a = getting_int("Please enter first number:\n")
b = getting_int("Please enter second number:\n")

try:
    c = a / b
    print(c)
except (ZeroDivisionError, ValueError,):
    print("No destroying entire universe this time pal")
    sys.exit(2)
finally:
    print("Thank you for using DIVISION MACHINE 3001!")


