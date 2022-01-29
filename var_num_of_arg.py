def sum_numbers(*num:float) -> float:

    """Returns sum of numbers"""
    result = 0
    for number in num:
        result += number
    return result

print(sum_numbers(float(input()), float(input()),float(input())))
