import random

from player import Player
from items import Item, HpPotion, MpPotion
from enemies import Enemy
from battle import Battle
from spells import Spell


def main():
    # create player
    name = input('What is your name?\n')
    player = Player(name)
    print(f'Welcome, {player.name}!')
    print('You are a level 1 adventurer.')
    print('You have 0 experience points.')
    print('You have 0 gold.')
    print('You have 100 HP and 100 MP.')
    print('You have no items.')
    print('You have no equipment.')
    print('You have no spells.')
    print('You have no quests.')
    print('You are in the starting area.')

    # create items
    potion = HpPotion('Potion', hp=15)
    ether = MpPotion('Mana Porion', mp=15)

    # create enemies
    slime = Enemy(name='Slime', hp=10, damage=1, exp=3, gold=5)
    goblin = Enemy(name='Goblin', hp=15, damage=2, exp=5, gold=10)
    enemies = [slime, goblin]

    # create spells
    fireball = Spell(name='Fireball', cost=10, damage=10)

    # add items, enemies, spells, and quests to player
    player.add_item(potion)
    player.add_item(ether)
    player.add_spell(fireball)

    # create battle
    random_enemy = random.choice(enemies)
    battle = Battle(player, random_enemy)
    battle.start()


if __name__ == '__main__':
    main()
