from player import Player

niko = Player("Niko")

print(niko.name)
print(niko.lives)
niko.lives -= 1
print(niko.lives)
niko.level = 5
print(niko)

from enemy import Enemy, Troll, Vampire, VampireKing

random_monster = Enemy("Basic enemy", 12, 1)
print(random_monster)

random_monster.take_damage(4)
print(random_monster)
random_monster.take_damage(8)
print(random_monster)

ugly_troll = Troll('Pug')
print("Ugly troll - {}".format(ugly_troll))

another_troll = Troll("Gug")
print("Another troll - {}".format(another_troll))
another_troll.take_damage(28)
print(another_troll)
dark_vampire = Vampire("Dark lord Kitten")

dark_vampire.take_damage(12)
print(dark_vampire)

dracula = VampireKing("Dracula")
print(dracula)
dracula.take_damage(12)
print(dracula)

