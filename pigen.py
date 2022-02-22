def oddnumbers():
    n = 1
    while True:
        yield n
        n += 2


def pi_series():
    odds = oddnumbers()
    approximation = 0
    while True:
        approximation += (4 / next(odds))
        yield approximation
        approximation -= (4/ next(odds))
        yield approximation


approx_pi = pi_series()

for x in range(200000000):
    print(next(approx_pi))

# for odd in range(100):
#     print(next(odds))