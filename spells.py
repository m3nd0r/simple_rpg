import random


class Spell:
    def __init__(self, name, cost, damage):
        self.name = name
        self.cost = cost
        self.damage = damage

    def generate_spell_damage(self):
        return random.randrange(abs(self.damage - 5), self.damage + 5)

    def use(self, player, enemy):
        player.remove_mp(self.cost)
        enemy.remove_hp(self.generate_spell_damage())
        print(f'You used {self.name}! You dealt {self.generate_spell_damage()} damage!')

    def __repr__(self):
        return f'{self.name}, {self.cost}, {self.damage}'
