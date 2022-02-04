# jabber = open("C:\\Users\\Nikodem\\desktop\\sample.txt", "r")
#
# for line in jabber:
#     print(line)
#
# jabber.close()
#
# with open("C:\\Users\\Nikodem\\desktop\\sample.txt", "r") as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
# #             print(line, end="")
# with open("C:\\Users\\Nikodem\\desktop\\sample.txt", "r") as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end="")
#         line = jabber.readline()
with open("C:\\Users\\Nikodem\\desktop\\sample.txt", "r") as jabber:
    lines = jabber.readlines()

for line in lines[::-1]:
    print(line, end='')