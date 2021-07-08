from pokemons import *
import random

print("Pokemon")
print("Oak: Select your first pokemon...")
[print(f"{i+1}.{pokemon.name}") for i, pokemon in enumerate(pokemons)]
user = int(input("Choose: ")) - 1
pokemon_a = pokemons[user]
print(pokemon_a)
# print (random.choice(pokemons))




