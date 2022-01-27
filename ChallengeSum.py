def sum_eo(n, t):
    n = int(input("Input max range of numbers string:\n"))
    t = input("Pick e for even numbers, o for odd numbers in range:\n")
    i = 0
    if 'e' in t:
        for num in range(1, n+1):
            if num % 2 == 0:
                i += num
        return i
    elif 'o' in t:
        for num in range(1, n+1):
            if num % 2 != 0:
                i += num
        return i
    else:
        return-1


n = 0
t = ""
number = sum_eo(n, t)
print(number)