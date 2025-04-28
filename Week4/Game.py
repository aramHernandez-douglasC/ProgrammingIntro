import random
from Pokemon import Pokemon

charizard = Pokemon("Charizard", 99, 999, 10, {
        "fireball": 3,
        "fireblast": 5,
        "fire-breath": 4 }
                    )
bulbasaur = Pokemon("Bulbasaur", 99, 999, 20, {
        "waterball": 3,
        "waterblast": 5,
        "water-breath": 4 }
                    )
pikachu = Pokemon("Pikachu", 99, 999, 30, {
        "thunderball": 3,
        "thunderblast": 5,
        "thunder-breath": 4 }
                    )
squirtle = Pokemon("Squirtle", 99, 999, 27, {
        "waterslap": 3,
        "water-hurricane": 1,
        "water-kamehameha": 4 }
                    )


class PokemonGame:

    def start(self):
        allPokemon = [charizard, bulbasaur, pikachu, squirtle]
        print("🎮 Welcome to Pokémon Battle Arena!")
        print("1. Charizard \n 2. Bulbasaur \n 3. Pikachu \n 4. Squirtle")
        hero_name = input("Choose your pokemon (from the deck 1-4): ")
        hero_name = int(hero_name)

        match hero_name:
            case 1:
                self.user_pokemon = charizard
            case 2:
                self.user_pokemon = bulbasaur
            case 3:
                self.user_pokemon = pikachu
            case 4:
                self.user_pokemon = squirtle
            case _ :
                print ("Not found select from 1 to 4")
                self.start()


        self.enemy = random.choice(allPokemon)
        print(f"\n✨ You chose {self.user_pokemon.name.capitalize()}!\n")
        self.battle_loop()

    def battle_loop(self):
        print(f"\n⚔️ Battle: {self.user_pokemon.name.capitalize()} vs {self.enemy.name.capitalize()}!")

        while self.user_pokemon.is_alive() and self.enemy.is_alive():
            print(f"Current stats: \n User: {self.user_pokemon.name} HP= {self.user_pokemon.health} "
                  f"\n CPU: {self.enemy.name} HP = {self.enemy.health} \n")
            action = input("Do you want to attack or heal? ").lower()

            if action == "attack":
                for key, value in self.user_pokemon.moves.items():
                    print(f"Power move: {key}. Potential Damage: {value}")
                selected_move = input("Select: ").lower()

                self.user_pokemon.attack(other=self.enemy, move=selected_move)

            elif action == "heal":
                heal_amount = random.randint(2, 5)
                self.user_pokemon.health += heal_amount
                print(f"{self.user_pokemon.name} healed for {heal_amount} HP!")

            else:
                print("Invalid action! You lost your turn!")

            if self.enemy.is_alive():
                self.enemy.attack(self.user_pokemon, random.choice(list(self.enemy.moves.keys())))

        if self.user_pokemon.is_alive():
            print(f"\n🎉 Congratulations, {self.user_pokemon.name.capitalize()}! You won the battle!")

        else:
            print("\n☠️ Game Over.")










