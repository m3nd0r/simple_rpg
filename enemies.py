import random


class Enemy:
    def __init__(self, name, hp, damage, exp, gold=0, lvl=1):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.exp = exp
        self.lvl = lvl
        self.gold = gold

    def is_alive(self):
        return self.hp > 0

    def remove_hp(self, hp):
        self.hp -= hp
        print(f'The {self.name} lost {hp} HP! It now has {self.hp} HP.')

    def generate_damage(self):
        return random.randrange(abs(self.damage - 5), self.damage + 5)

    def generate_exp(self):
        return random.randrange(abs(self.exp - 5), self.exp + 5)

    def __repr__(self):
        return f'{self.name}, {self.hp}, {self.damage}, {self.exp}'
