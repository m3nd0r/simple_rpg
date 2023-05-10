class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def start(self):
        print(f'You have encountered a {self.enemy.name}!')
        while self.player.hp > 0 and self.enemy.hp > 0:
            print(f'You have {self.player.hp} HP and {self.player.mp} MP.')
            print(f'The {self.enemy.name} has {self.enemy.hp} HP.')
            print('What would you like to do?')
            print('1. Attack')
            print('2. Use Item')
            print('3. Use Magic')
            choice = input()
            if choice == '1':
                self.attack()
            elif choice == '2':
                self.use_item()
            elif choice == '3':
                self.use_magic()
            else:
                print('Invalid choice.')
        if self.player.hp <= 0:
            print('You have died.')
        elif self.enemy.hp <= 0:
            print(f'You have defeated the {self.enemy.name}!')
            self.player.add_exp(self.enemy.exp)
            self.player.add_gold(self.enemy.gold)

    def attack(self):
        self.enemy.remove_hp(self.player.damage)
        if self.enemy.hp > 0:
            self.player.remove_hp(self.enemy.damage)

    def use_item(self):
        if len(self.player.inventory) == 0:
            print('You have no items.')
        else:
            print('Which item would you like to use?')
            for item in self.player.inventory:
                print(item)
            choice = input()
            for item in self.player.inventory:
                if item.name == choice:
                    item.use(self.player)
                    self.player.remove_item(item)
                    break
                else:
                    print('Invalid choice.')

    def use_magic(self):
        if len(self.player.spells) == 0:
            print('You have no spells.')
        else:
            print('Which spell would you like to use? Type the name of the spell.')
            for spell in self.player.spells:
                print(spell)
            choice = input()
            for spell in self.player.spells:
                if spell.name == choice:
                    spell.use(self.player, self.enemy)
                    break
                else:
                    print('Invalid choice.')
