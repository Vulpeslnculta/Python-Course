def sum_numbers(*num:float) -> float:
    """Returns sum of numbers"""
    a, b, c = num
    d = a + b + c
    return d


print(sum_numbers(float(input()), float(input()),float(input())))