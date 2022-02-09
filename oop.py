class Kettle(object):

    power_source = 'elecricity'


    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)
kenwood.price = 19.75
print(kenwood.price)

hamilton = Kettle('Hamilton', 14.55)
print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))

print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)
print(hamilton.on)

kenwood.power = 1.5
print(kenwood.power)
# print(hamilton.power)

print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)