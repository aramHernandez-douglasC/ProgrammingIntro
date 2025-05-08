import Character
from GPTService import GPTService
import Pokemon

class GPTBattleService:
    def __init__(self):
        self.gpt_service = GPTService()

    def generate_battle_narration(self, attacker, move, defender, damage):
        prompt = (
            f"{attacker} uses {move} on {defender}, dealing {damage}! Narrate this in a fun Pokemon battle style similar to vete a la versh videos"
            "use spanish"
        )
        system_prompt = "You are a Pokemon battle style narrator."
        return self.gpt_service.chat(system_prompt, prompt)

    def suggest_next_move(self, character: Character, enemy: Character):
        prompt = (
            f"My pokemon is {character.pokemon.name} with types {character.pokemon.types} and {character.pokemon.health} HP \n"
            f"The enemy is {enemy.pokemon.name} with types {enemy.pokemon.types} and {character.pokemon.health} HP \n"
            f"Available moves are: {character.pokemon.moves} \n"
            "Which move should I use"
        )
        return self.gpt_service.chat("You are pokemon strategist.", prompt)

    def choose_gpt_move(self, character: Character, opponent: Character) -> int:
        prompt = (
            f"You are a Pokémon battle expert controlling {character.pokemon.name}. "
            f"{character.pokemon.name} has {character.pokemon.health} HP and types {character.pokemon.types}.\n"
            f"Available moves: {character.pokemon.moves.keys()}.\n"
            f"The opponent is {opponent.pokemon.name} with {opponent.pokemon.health} HP and types {opponent.pokemon.types}.\n"
            "Which move should you use to maximize effectiveness? Just respond with the exact move name."
            "Use spanish"

        )
        reply = self.gpt_service.chat("You are a pokemon startegist", prompt).lower()

        # TODO: Fix this to take in a dictionary
        for key in character.pokemon.moves:
            if key in reply:
                return key

        return list(character.pokemon.moves)[0]

    def generate_enemy_taunt(self, player_move: str, player_pokemon: Pokemon, enemy_pokemon: Pokemon):

        prompt = (
            f"You are a cocky and despicable rival Pokémon trainer similar to vete a la versh videos.\n"
            f"The opponent used '{player_move}' with their Pokémon {player_pokemon.name}, HP: {player_pokemon.health}.\n"
            f"Your Pokémon is {enemy_pokemon.name} with HP: {enemy_pokemon.health}.\n"
            "React sarcastically, mocking their move. If your Pokémon has less than 20 HP, react nervously instead."
            "Use spanish"
        )
        return self.gpt_service.chat("You are a cocky rival trainer.", prompt)
