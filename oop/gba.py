from pokemons import *
import random

print("Pokemon")
print("Oak: Select your first pokemon...")
[print(f"{i+1}.{pokemon.name}") for i, pokemon in enumerate(pokemons)]
user = int(input("Choose: ")) - 1
pokemon_a = pokemons[user]
print(pokemon_a)
 
pokemons.remove(pokemon_a)
oponent = random.choice(pokemons)
print(f"Your oponent is {oponent.name}")


while oponent.is_alive:
    for i, attack in enumerate(pokemon_a.attacks):
        print(f"{i+1}.{attack.name}")
    user = int(input("Choose: ")) - 1
    oponent.receive_damage(pokemon_a.attacks[user])
    print(oponent)

print ("El pokemon murió")