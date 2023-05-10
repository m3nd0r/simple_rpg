class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.level = 1
        self.hp = 100
        self.mp = 100
        self.exp = 0
        self.gold = 0
        self.inventory = []
        self.equipment = []
        self.spells = []
        self.quests = []
        self.damage = self.calculate_damage() if self.equipment else 10
        self.location = None

    def __str__(self) -> str:
        return self.name

    def add_item(self, item) -> None:
        self.inventory.append(item)

    def add_quest(self, quest) -> None:
        self.quests.append(quest)

    def add_exp(self, exp: int) -> None:
        self.exp += exp
        print(f'You gained {exp} experience points!')
        if self.exp > 100:
            self.level += 1
            self.exp = 0
            print(f'You leveled up to level {self.level}!')

    def add_gold(self, gold: int) -> None:
        self.gold += gold
        print(f'You gained {gold} gold!')

    def add_hp(self, hp: int) -> None:
        self.hp += hp
        print(f'You healed for {hp} HP! You now have {self.hp} HP.')

    def add_mp(self, mp: int) -> None:
        self.mp += mp
        print(f'You gained {mp} MP! You now have {self.mp} MP.')

    def add_equipment(self, equipment):
        self.equipment.append(equipment)

    def add_spell(self, spell):
        self.spells.append(spell)

    def remove_item(self, item):
        self.inventory.remove(item)

    def remove_quest(self, quest):
        self.quests.remove(quest)

    def remove_equipment(self, equipment):
        self.equipment.remove(equipment)

    def remove_hp(self, hp):
        self.hp -= hp
        print(f'You lost {hp} HP! You now have {self.hp} HP.')

    def remove_mp(self, mp):
        self.mp -= mp
        print(f'You lost {mp} MP! You now have {self.mp} MP.')

    def remove_gold(self, gold):
        self.gold -= gold
        print(f'You lost {gold} gold!')

    def remove_spell(self, spell):
        self.spells.remove(spell)

    def remove_exp(self, exp):
        self.exp -= exp
        print(f'You lost {exp} experience points!')

    def remove_level(self, level):
        self.level -= level
        print(f'You lost {level} levels!')

    def remove_damage(self, damage):
        self.damage -= damage
        print(f'You lost {damage} damage!')

    def calculate_damage(self):
        total = 10
        for equipment in self.equipment:
            if equipment.damage is not None:
                total += equipment.damage
        return total
