n = input("Please input maximal value of chart: \n")
n = int(n) + 1
for i in range (1, n):
    for j in range(1, n):
        print("{0} times {1} is {2}".format(j, i, i*j))
        print("________________________________")
    print("\n________________________________\n")