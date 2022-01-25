welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])
metallica2 = list(metallica)
print(metallica2)
#  List are mutables type of data, Tuples aren't

metallica2[0] = "Master of Puppets"
metallica2 = tuple(metallica2)
print(metallica2)