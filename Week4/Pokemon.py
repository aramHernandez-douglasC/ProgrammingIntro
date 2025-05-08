import random

class Pokemon:
    def __init__(self, name: str, height: int, weight: int, health: int, moves: dict, types: list[str] = []):
        self.name = name
        self.height = height
        self.weight = weight
        self.health = health
        self.moves: dict = moves
        self.types = types

    def is_alive(self):
        return self.health > 0

    def attack(self, other, move):
        if ((move)) not in self.moves:
            print(f"Move doesn't exist. You take damage of one of your attacks!")
            damage = random.randint(2 // 2, 2)
            self.health -= damage
        else:
            power = self.moves.get(move)
            damage = random.randint(power // 2, power)
            other.health -= damage
            print(f"{self.name} uses {move}! It deals {damage} to {other.name}!")

        return damage