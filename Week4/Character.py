
class Character:
    def __init__(self, name: str, role: str, pokemon):
        self.name = name
        self.role = role
        self.pokemon = pokemon

    def change_pokemon(self, new_pokemon):
        old_pokemon = self.pokemon
        self.pokemon = new_pokemon
        print(f"{self.name} just change their pokemon from {old_pokemon} to {new_pokemon}")


class Enemy(Character):
    def __init__(self, name: str, role: str, pokemon, personality: str):
        Character.__init__(self, name, role, pokemon)
        self.personality = personality


class Narrator(Character):
    def __init__(self, name: str, role: str, pokemon, personality: str, surprise_level: int):
        Character.__init__(self, name, role, pokemon)
        self.personality = personality
        self.surprise_level = surprise_level


