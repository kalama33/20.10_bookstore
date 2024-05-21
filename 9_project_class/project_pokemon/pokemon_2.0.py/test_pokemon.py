from pokemones import Pokemon, AttackSkill
import random

pikachu = Pokemon("Pikachu", 150, 220) # instances
bulbasaur = Pokemon("Bulbasaur", 150, 220)
jiglipuf = Pokemon("Jiglipuf", 200, 130)

lightning = AttackSkill("Lightning", 25, 20) # instances
poison_seed = AttackSkill("PoisonSeed", 20, 25)
chant = AttackSkill("Chant", 30, 20)

pikachu.learn_attack_skill(lightning) # method from pokemon class to get skills
pikachu.learn_attack_skill(poison_seed)

bulbasaur.learn_attack_skill(lightning)
bulbasaur.learn_attack_skill(poison_seed)

jiglipuf.learn_attack_skill(lightning)
jiglipuf.learn_attack_skill(chant)

print("POKEMON'S BATTLE")
print()


def choose_pokemon(): #function for the user to choose a Pokemon
    print("Choose your character:\n")
    print("1. Pikachu\n")
    print("2. Bulbasaur\n")
    print("3. Jiglipuf\n")
    choice = input("Enter the number corresponding to the pokemon you want:")
    
    if choice == "1":
        return pikachu
    elif choice == "2":
        return bulbasaur 
    elif choice == "3":
        return jiglipuf
    else:
        print("Invalid selection. Defaulting to Pikachu.\n")
        return pikachu # by default
    
