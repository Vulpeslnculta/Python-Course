albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Emilda May", 2011),
          ("Ride the Lightning", "Metallica", 1984),
          ]

print(len(albums))

for album in albums:
    name = album[0]
    artist = album[1]
    year = album[2]
    print("Album: {}, Artist: {}, Year: {}".format(name, artist, year))
print()
#  Same output, slightly different result
for name, artist, year in albums:
    print("Album: {}, Artist: {}, Year: {}".format(name, artist, year))