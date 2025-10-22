import random

#Choosing Pokemons
pokemonsDex = [
    {"Pikachu": {"number": "1", "type1": "Electric", "type2": ""}},
    {"Blastoise": {"number": "2", "type1": "Water", "type2": ""}},
    {"Bulbasaur": {"number": "3", "type1": "Grass", "type2": "Poison"}},
    {"Hauntly": {"number": "4", "type1": "Ghost", "type2": "Poison"}},
    {"Squirtle": {"number": "5", "type1": "Water", "type2": ""}},
    {"Ponyta": {"number": "6", "type1": "Fire", "type2": ""}}
]

def get_pokemon(name): #
    for p in pokemonsDex:
        if name in p:
            return p[name]
    return None

def GetUserInput():
    """Ask user to pick a Pokémon until a valid one is chosen."""
    while True:
        playerChoice = input("Pick a Pokémon: ").capitalize()
        for pokemon in pokemonsDex:
            if playerChoice in pokemon:
                print(f"You have picked: {playerChoice}")
                return playerChoice
        print("That is not a Pokémon! Try again.")


# Battle
def battle(player_pokemon_name, enemy_pokemon_name):
    player = get_pokemon(player_pokemon_name)
    enemy = get_pokemon(enemy_pokemon_name)

    if not player or not enemy:
        print("One of the Pokémon names is invalid.")
        return

    player_hp = 50
    enemy_hp = 50

    print(f"\n {player_pokemon_name} (You) vs {enemy_pokemon_name} (Enemy)")
    print(f"Your type: {player['type1']} {player['type2']}")
    print(f"Enemy type: {enemy['type1']} {enemy['type2']}\n")

    while player_hp > 0 and enemy_hp > 0:
        print(f"Your HP: {player_hp} | Enemy HP: {enemy_hp}")
        action = input("(A)ttack or (H)eal? ").lower()

        if action == "a":
            base_damage = random.randint(8, 15)
            total_damage = base_damage 
            enemy_hp -= total_damage
            print(f"\n You attack! You dealt {total_damage} damage!")
        elif action == "h":
            heal = random.randint(5, 10)
            player_hp += heal
            print(f"\n You heal for {heal} HP!")
        else:
            print("\nYou fumbled and lost your turn!")

        if enemy_hp <= 0:
            print(f"\n {enemy_pokemon_name} fainted! You win!")
            break

        #Enemy attack
        enemy_base = random.randint(6, 12)
        total_damage = enemy_base
        player_hp -= total_damage
        print(f"The enemy attacks for {total_damage} damage!")

        if player_hp <= 0:
            print(f"\n {player_pokemon_name} fainted! You lose!")

    print("\n=== Battle Over ===")

    while True:
        play_again = input("Would you like to start a new battle? (y/n): ").strip().lower()
        if play_again in ['yes','y']:
            return True
        elif play_again in ['no','n']:
            return False
        else:
            print("Invalid input. Please enter y or n")


while True:
    print("You have entered a battle")
    player_choice = GetUserInput()

    # Random enemy Pokémon that isn’t yours
    available_enemies = [list(p.keys())[0] for p in pokemonsDex if player_choice not in p]
    enemy_choice = random.choice(available_enemies)

    print(f"Your opponent will be {enemy_choice}!")
    continue_playing = battle(player_choice, enemy_choice)

    if not continue_playing:
        print("Thanks for playing")
        break