#pokemon game

print("\n############################")
print("#### POKEMON BATTLE #####")
print("##########################\n")

print("Available Pokemons: Pikachu, Bulbasaur, Blastoise, Hauntly, Squirtle, Ponyta  ")

#POKEMONS
pokemonsDex = [
{"Pikachu":{"number":"1", "type1":"electric", "type2":""}},
{"Blastoise":{"number":"2", "type1":"water", "type2":""}},
{"Bulbasaur":{"number":"3", "type1":"grass", "type2":"poison"}},
{"Hauntly":{"number":"4", "type1":"ghost", "type2":"poison"}},
{"Squirtle":{"number":"5", "type1":"water", "type2":""}},
{"Ponyta":{"number":"6", "type1":"fire", "type2":""}},
]

#USER INPUT
def GetUserInput():
    while True:
        playerChoice = input("Pick a Pokemon: ")
        found = False
        for pokemon in pokemonsDex:
            if playerChoice in pokemon:
                print(f"You have picked: {playerChoice}")
            found = True
            break
        if not found:
            print("That is not a Pokemon!")

#MOVESETS
pika_moveset = ["Thunder Shock" , "Quick Attack", "Thunderbold" , "Slam"]
blas_moveset = ["Skull Bash", "Hydro Pump", "Bite", "Earthquake"]
bulb_moveset = ["Poison Powder", "Solar Beam", "Vine Whip", "Razor Leaf"]
haun_moveset = ["Dream Eater", "Lick", "Confuse Ray", "Mimic"]
squi_moveset = ["Dig", "Mega Punch", "Withdraw", "Bubble"]
pony_moveset = ["Agility", "Take Down", "Stomp", "Fire Spin"]

#ATTACKS
def PokemonAttack():
