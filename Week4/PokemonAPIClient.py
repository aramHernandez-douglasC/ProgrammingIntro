import random

import requests
from Pokemon import Pokemon

class PokemonAPIClient:
    BASE_URL = "https://pokeapi.co/api/v2/pokemon/"

    def get_pokemon(self, name: str):
        response = requests.get(self.BASE_URL + name.lower()) #  https://pokeapi.co/api/v2/pokemon/pikachu

        if response.status_code == 500:
            print(f"Pokemon {name} had an issue retrieving")
            return

        data = response.json()

        health = data['stats'][0]['base_stat']
        moves = {}
        for move in data['moves'][:5]:
            move_name = move['move']['name']
            power = random.randint(5, 30)
            moves[move_name] = power

        return Pokemon(
            name = data['name'],
            health = health,
            moves = moves,
            height = 0,
            weight= 0
        )
