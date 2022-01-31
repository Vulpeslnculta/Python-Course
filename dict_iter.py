vehicles = {
    'dream': 'Yamaha YZF-R1',
    'roadster': 'BMW R1100s',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4'
}
vehicles["starfighter"] = "Lockheed F-104"
vehicles["learjet"] = "Bombardier Learjet"
vehicles["toy"] = "Glider"

# for key in vehicles:
#     print(key, vehicles[key], sep=" - ")
for key, value in vehicles.items():
    print(key, value, sep=" - ")

print("_"*80)

vehicles["virago"] = "Yamaha XV650"

del vehicles["starfighter"]
result = vehicles.pop("f1", "You are too poor for that, mate")
print(result)
plane = vehicles.pop("learjet")
print(plane)

bike = vehicles.pop("tenere", "Do not exist")
print(bike)
print("_"*80)
for key, value in vehicles.items():
    print(key, value, sep=" - ")