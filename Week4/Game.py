import random
from PokemonAPIClient import PokemonAPIClient
from Character import Character, Enemy
from GPTBattleService import GPTBattleService

class PokemonGame:

    def __init__(self):
        self.pokemonApi = PokemonAPIClient()
        self.gptBattleService = GPTBattleService()

    def start(self):
        print("🎮 Welcome to Pokémon Battle Arena!")
        user_name = input("What is your name?")
        user_hero_name = input("Choose a pokemon").lower()
        user_pokemon = self.pokemonApi.get_pokemon(user_hero_name)

        self.userChar = Character(name=user_name, role="user", pokemon=user_pokemon)

        enemy_pokemon = self.pokemonApi.get_pokemon(random.randint(0, 500))

        self.enemyChar = Enemy(name="juan", role="enemy", pokemon=enemy_pokemon, personality="cocky")
        print(f"\n✨ You chose {self.userChar.pokemon.name.capitalize()}!\n")
        self.battle_loop()

    def battle_loop(self):
        print(
            f"\n⚔️ Battle: {self.userChar.name.capitalize()} vs {self.enemyChar.name.capitalize()}! \n"
            f"With Pokemons {self.userChar.pokemon.name.capitalize()} vs {self.enemyChar.pokemon.name.capitalize()}"
        )

        while self.userChar.pokemon.is_alive() and self.enemyChar.pokemon.is_alive():
            print(f"Current stats: \n User: {self.userChar.pokemon.name} HP= {self.userChar.pokemon.health} "
                  f"\n CPU: {self.enemyChar.pokemon.name} HP = {self.enemyChar.pokemon.health} \n")

            action = input("Do you want to attack or heal? ").lower()

            suggestion_response = self.gptBattleService.suggest_next_move(self.userChar, self.enemyChar)
            print(f"Suggestion attack: {suggestion_response}")

            if action == "attack":
                for key, value in self.userChar.pokemon.moves.items():
                    print(f"Power move: {key}. Potential Damage: {value}")
                selected_move = input("Select: ").lower()

                self.userChar.pokemon.attack(other=self.enemyChar.pokemon, move=selected_move)
                taunt = self.gptBattleService.generate_enemy_taunt(
                    player_pokemon=self.userChar.pokemon,
                    player_move=selected_move,
                    enemy_pokemon=self.enemyChar.pokemon
                )

                print(f"\n{taunt}")

            elif action == "heal":
                heal_amount = random.randint(2, 5)
                self.userChar.pokemon.health += heal_amount
                print(f"{self.userChar.pokemon.name} healed for {heal_amount} HP!")

            else:
                print("Invalid action! You lost your turn!")

            if self.enemyChar.pokemon.is_alive():
                self.enemy_turn()

        if self.userChar.pokemon.is_alive():
            print(f"\n🎉 Congratulations, {self.userChar.pokemon.name.capitalize()}! You won the battle!")

        else:
            print("\n☠️ Game Over.")

    def enemy_turn(self):
        print("Enemy time {thinking ...}")
        enemy_move = self.gptBattleService.choose_gpt_move(self.enemyChar, self.userChar)
        enemy_result = self.enemyChar.pokemon.attack(other=self.userChar.pokemon, move=enemy_move)

        narration = self.gptBattleService.generate_battle_narration(
            attacker=self.enemyChar.pokemon.name,
            move=enemy_move,
            defender=self.userChar.pokemon.name,
            damage=enemy_result
        )

        print(narration)