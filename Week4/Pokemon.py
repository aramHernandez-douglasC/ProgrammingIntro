import random

class Pokemon:
    def __init__(self, name: str, height: int, weight: int, health: int, moves: dict):
        self.name = name
        self.height = height
        self.weight = weight
        self.health = health
        self.moves = moves

    def is_alive(self):
        return self.health > 0

    def attack(self, other, move):
        if move not in self.moves:
            print(f"Move doesn't exist. You take damage of one of your attacks!")
            damage = random.randint(2 // 2, 2)
            self.health -= damage
        else:
            power = self.moves.get(move)
            damage = random.randint(power // 2, power)
            other.health -= damage
            print(f"{self.name} uses {move}! It deals {damage} to {other.name}!")


class Pikachu(Pokemon):
    def __init__(self, name, height, weight, health, moves, type):
        Pokemon.__init__(self, name, height, weight, health, moves)
        self.type = type

    def attack(self, other, move):
        if move not in self.moves:
            print(f"move doesn't exist. You take damage of one of your attacks!")
            damage = random.randint(2 // 2, 2)
            self.health -= damage
        else:
            move_name, power = move
            damage = random.randint(power // 2, power)
            other.health -= damage
            print(f"{self.name} uses {move_name}! It deals {damage} to {other.name}!")

    def transform(self):
        print(f"Now you are of type: {self.type}")