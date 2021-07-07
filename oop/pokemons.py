# Pokemon
# https://pokeapi.co/
# types: fire, grass, water
# Crear clase Pokemon con los siguientes atributos y métodos

# name
# type
# HP
# attacks []
# Métodos: learn_attack, attack, receive_damage
# Crear clase Attack con los siguientes atributos
# name
# element
# damage
# Crear un pequeño menú que permita simular una batalla pokemon

elements = ["fire", "grass", "water"]
class Pokemon:
    def __init__(self, name, element, HP):
        self.name = name
        self.element = element
        self.HP = HP
        self.attacks = []

    def __str__(self):
        return f"name: {self.name}\ntype:{self.element}\nHP:{self.HP}\nattacks:{self.attacks}"

    def learn(self, attack):
        self.attacks.append(attack)



class Attack:

    def __init__(self, name, element, damage):
        self.name = name
        self.element = element
        self.damage = damage
    
    def __repr__(self): #repr se usa cuando no sea un str #su proposito es la manera de impresion del ataque
        return f"{self.name}"




charmander = Pokemon("Charmander", elements[0], 120)
squirtle = Pokemon("Squirtle", elements[2], 140 )
bulbasaur = Pokemon("Bulbasaur", elements[1], 160)

flamethrower = Attack("flamethrower", elements[0], 40)
razor_leaf = Attack("razor_Leaf", elements[1], 25)
surf = Attack("surf", elements[2], 35)


print (charmander) #print llama a str por detrás por eso no hay que ponerla necesariamente
print (squirtle)
print (bulbasaur)

charmander.learn(flamethrower)