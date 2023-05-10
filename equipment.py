class Equipment:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight
        self.equipped = False
        self.hp = 0
        self.mp = 0
        self.damage = None

    def __str__(self):
        return f'{self.name} - {self.price} - {self.weight}'
