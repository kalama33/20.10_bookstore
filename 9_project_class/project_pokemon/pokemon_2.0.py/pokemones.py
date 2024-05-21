import random


# attackskill, 3 atributes
class AttackSkill:
    def __init__(self, attack, damage, magic):
        self.attack = attack
        self.damage = damage
        self.magic = magic

    def __repr__(self):
        return f"{self.attack} {self.damage} {self.magic}"


# pokemon
# number that starts at 0 and increments every time the Pokemon launches a successful attack.

class Pokemon:
    def __init__(self, name, health, magic):
        self.name = name
        self.health = health
        self.magic = magic
        self.skills = []
        self.counter = 0

    # method accepts an object of the AttackSkill class and adds it to the skills list.

    def learn_attack_skill(self, skill):
        self.skills.append(skill)

    """
    This method prints the current health and magic of the Pokemon, and whether it has won the battle already, 
    based on the counter (a Pokemon is considered to have won if the counter is greater than 3).
    """  
    
    def show_status(self):
        print(f"{self.name}: Health: {self.health}, Magic: {self.magic}\n")
        if self.counter > 3:
            print(f"{self.name} is a powerful creature!")
        print()

    # increases the Pokemon's magic by a random number between 0 and 20.

    def get_magics(self):
        self.magic += random.randint(0, 20)
        
    # method checks if the Pokemon has enough magic to perform an attack skill.
    # It returns True if the magic is enough and False otherwise.

    def has_enough_magic(self, skill_name):
        for skill in self.skills:
            if skill.attack == skill_name:
                #print(self.magic, "- Magic Remaining\n")
                #print(skill.magic, "- Magic Used\n")
                return self.magic >= skill.magic
        return False

    """ 
    simulates an attack from the Pokemon to an opponent Pokemon. 
    It checks if both the attacking Pokemon and the opponent are alive 
    and if the attacking Pokemon has enough magic to perform the attack. 
    If the conditions are met, it decreases the attacking Pokemon's magic 
    and the opponent's health based on the selected attack skill. 
    It also increments the counter and calls the show_status method for both Pokemon.
    """
        
    def is_alive(self):
        return self.health > 0

    def attack(self, skill_name, opponent):
        if not self.is_alive():
            print(f"{self.name} is unable to attack. It has been defeated.\n")
            return

        if not opponent.is_alive():
            print(f"{opponent.name} is already defeated.\n")
            return

        selected_skill = None
        for skill in self.skills:
            if skill.attack == skill_name:
                selected_skill = skill
                break

        if selected_skill is None:
            print(f"{self.name} does not know the attack skill: {skill_name}.\n")
            return

        if not self.has_enough_magic(skill_name):
            print(f"{self.name} does not have enough magic to use {skill_name}.\n")
            return

        self.magic -= selected_skill.magic
        opponent.health -= selected_skill.damage
        self.counter += 1

        print(f"{self.name} attacked {opponent.name} with {skill_name}.\n")
        print(f"{opponent.name} lost {selected_skill.damage} health points.\n")
        self.show_status()
        opponent.show_status()
        
        
"""
# create new pokemons (instances)
pikachu = Pokemon("pikachu", 150, 200)
bulbasaur = Pokemon("bulbasaur", 130, 220)

# create new skills that Pokemons can learn (instances)
lightning = AttackSkill("lightning", 25, 25)
bombing = AttackSkill("poisonSeed", 20, 20)

# pikachu learning skills/method learn_attack_skill
pikachu.learn_attack_skill(lightning)
pikachu.learn_attack_skill(bombing)

# bulbasaur learning skills
bulbasaur.learn_attack_skill(lightning)
bulbasaur.learn_attack_skill(bombing)

# Pokemons start attacking each other/method atack and opponent
pikachu.attack("lightning", bulbasaur)
print() 
bulbasaur.attack("poisonSeed", pikachu)
print() 
pikachu.attack("poisonSeed", bulbasaur)
print() 
bulbasaur.attack("lightning", pikachu)
print() 
pikachu.attack("lightning", bulbasaur)
print() 
pikachu.attack("poisonSeed", bulbasaur)  
"""  