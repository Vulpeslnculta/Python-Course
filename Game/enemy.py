class Enemy(object):

    def __init__(self, name='Enemy', hit_points=0, lives=1):
        self._name = name
        self._hit_points = hit_points
        self.lives = lives

    def take_damage(self, damage):
        HP = self._hit_points
        remaining_points = self._hit_points - damage
        if remaining_points > 0:
            self._hit_points = remaining_points
            print("Ugh, I took {} points of damage, and I have {} health left!".format(damage, remaining_points))
        else:
            self._hit_points = remaining_points
            self.lives -= 1
            print("BLEH, I'M DEAD")
            if self.lives >= 1:
                print("OR AM I?")
                self._hit_points = HP


    def __str__(self):
        return "Name: {0._name}, Lives: {0.lives}, Hit points: {0._hit_points}".format(self)


class Troll(Enemy):
    def __init__(self, name):
        super().__init__(name=name, lives=1, hit_points=28)


class Vampire(Enemy):
    def __init__(self, name):
        super().__init__(name=name, lives=3, hit_points=12)

    def dodge(self):
        import random
        if random.randint(1, 3) == 3:
            print("__ {0._name} dodges your attack __".format(self))
            return True
        else:
            print("__ {0._name} tried to dodge your attack __\n__ But it fails! __".format(self))
            return False

    def take_damage(self, damage):
        if not self.dodge():
            super().take_damage(damage=damage)


class VampireKing(Vampire):
    def __init__(self, name):
        super().__init__(name)
        self._hit_points = 140

    def take_damage(self, damage):
        super().take_damage(damage // 4)


