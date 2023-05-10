class Item:
    def __init__(self, name, description='', quantity=1):
        self.name = name
        self.description = description
        self.quantity = quantity

    def __str__(self):
        return f'{self.name}: {self.description}'

    def use(self, player):
        pass


class HpPotion(Item):
    def __init__(self, name, description='', quantity=1, hp=15):
        super().__init__(name, description, quantity)
        self.hp = hp

    def use(self, player):
        player.add_hp(self.hp)
        print(f'You used a {self.name}! You gained {self.hp} HP!')


class MpPotion(Item):
    def __init__(self, name, description='', quantity=1, mp=15):
        super().__init__(name, description, quantity)
        self.mp = mp

    def use(self, player):
        player.add_mp(self.mp)
        print(f'You used a {self.name}! You gained {self.mp} MP!')
