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

my_bike = vehicles['dream']
print(my_bike)

commuter = vehicles['virago']
print(commuter)

learner = vehicles.get('er5')
print(learner)
