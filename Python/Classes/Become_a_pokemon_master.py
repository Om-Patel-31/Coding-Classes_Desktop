class Pokemon:
    def __init__(self, name, level, type):
        self.name = name
        self.level = level
        self.type = type
        self.max_health = level * 10
        self.current_health = self.max_health
        self.is_knocked_out = False
        self.experience = 0

    def __str__(self) -> str:
        return f"{self.name} (Level: {self.level}, Type: {self.type}, Health: {self.current_health}/{self.max_health}, Knocked Out: {self.is_knocked_out})"

    def lose_health(self, amount):
        if self.is_knocked_out:
            print(f"{self.name} is knocked out and cannot lose more health")
            return
        self.current_health -= amount
        if self.current_health <= 0:
            self.current_health = 0
            self.knock_out()
        else:
            print(f"{self.name} has lost {amount} health and now has {self.current_health}/{self.max_health} health.")

    def gain_health(self, amount):
        if self.is_knocked_out:
            print(f"{self.name} is knocked out and cannot gain health. Use revive first.")
            return
        self.current_health += amount
        if self.current_health > self.max_health:
            self.current_health = self.max_health
        print(f"{self.name} now has {self.current_health} health after gaining {amount} health.")

    def knock_out(self):
        if not self.is_knocked_out:
            self.is_knocked_out = True
            self.current_health = 0
            print(f"{self.name} is knocked out.")

    def revive(self):
        if self.is_knocked_out:
            self.is_knocked_out = False
            self.current_health = self.max_health // 2
            print(f"{self.name} has been revived with {self.current_health}/{self.max_health}.")
        else:
            print(f"{self.name} is not knocked out and does not need to be revived.")

    def attack(self, other_pokemon):
        if self.is_knocked_out:
            print(f"{self.name} is knocked out and cannot attack.")
            return
        damage = self.level
        if (self.type == "Fire" and other_pokemon.type == "Grass") or \
           (self.type == "Water" and other_pokemon.type == "Fire") or \
           (self.type == "Grass" and other_pokemon.type == "Water"):
            damage *= 2
            print(f"{self.name} attacks {other_pokemon.name} with a type advantage!")
        elif (self.type == "Fire" and other_pokemon.type == "Water") or \
             (self.type == "Water" and other_pokemon.type == "Grass") or \
             (self.type == "Grass" and other_pokemon.type == "Fire"):
            damage /= 2
            print(f"{self.name} attacks {other_pokemon.name} with a type disadvantage!")
        print(f"{self.name} deals {damage} damage to {other_pokemon.name}.")
        other_pokemon.lose_health(damage)
        self.gain_experience(10)
    
    def gain_experience(self, exp):
        self.experience += exp
        print(f"{self.name} has gained {exp} experience points.")
        if self.experience >= self.level * 50:
            self.level_up()
            
    def level_up(self):
        self.level += 1
        self.max_health = self.level * 10
        self.current_health = self.max_health
        self.experience = 0
        print(f"{self.name} leveled up! Now at level {self.level}.")

class Charmander(Pokemon):
    def __init__(self, level):
        super().__init__("Charmander", level, "Fire")

class Bulbasaur(Pokemon):
    def __init__(self, level):
        super().__init__("Bulbasaur", level, "Grass")

class Squirtle(Pokemon):
    def __init__(self, level):
        super().__init__("Squirtle", level, "Water")
        

class Trainer:
    def __init__(self, name, pokemons, potions):
        self.name = name
        self.pokemons = pokemons[:6]
        self.potions = potions
        self.current_pokemon = 0
    
    def __str__(self) -> str:
        pokemon_list = ', '.join([pokemon.name for pokemon in self.pokemons])
        return f"{self.name} has the following Pokemon: {pokemon_list}. Currently Active Pokemon is {self.pokemons[self.current_pokemon].name}."

    def use_potion(self):
        if self.potions > 0:
            active_pokemon = self.pokemons[self.current_pokemon]
            if active_pokemon.is_knocked_out:
                print(f"{active_pokemon.name} is knocked out and cannot be healed. Use revive first.")
            else:
                self.potions -= 1
                active_pokemon.gain_health(20)
                print(f"{self.name} used a potion on {active_pokemon.name}.")
        else:
            print(f"{self.name} has no potions left.")
    
    def attack_trainer(self, other_trainer):
        my_pokemon = self.pokemons[self.current_pokemon]
        other_pokemon = other_trainer.pokemons[other_trainer.current_pokemon]
        print(f"{self.name}'s {my_pokemon.name} attacks {other_trainer.name}'s {other_pokemon.name}!")
        my_pokemon.attack(other_pokemon)
    
    def switch_pokemon(self, new_pokemon_index):
        if new_pokemon_index < 0 or new_pokemon_index >= len(self.pokemons):
            print("Invalid Pokemon Index.")
            return
        if self.pokemons[new_pokemon_index].is_knocked_out:
            print(f"{self.pokemons[new_pokemon_index].name} is knocked out and cannot be switched in.")
            return
        self.current_pokemon = new_pokemon_index
        print(f"{self.name} switched to {self.pokemons[self.current_pokemon].name}.")
       
def test_examples():
    charmender = Charmander(5)
    bulbasaur = Bulbasaur(5)
    squirtle = Squirtle(5)

    print(charmender)
    print(bulbasaur)
    print(squirtle)

    charmender.attack(bulbasaur)
    bulbasaur.attack(charmender)
    squirtle.attack(charmender)
    print(charmender)

    trainer1 = Trainer("Ash", [charmender, bulbasaur], 3)
    trainer2 = Trainer("Misty", [squirtle], 2)

    print(trainer1)
    print(trainer2)

    trainer1.attack_trainer(trainer2)
    trainer2.use_potion()
    trainer1.switch_pokemon(1)
    trainer1.attack_trainer(trainer2)
    trainer2.use_potion()
    trainer1.attack_trainer(trainer2)
    trainer2.use_potion()

test_examples()