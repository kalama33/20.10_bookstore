from pokemon import Pokemon, AttackSkill
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


print("POKEMON'S BATTLE\n")


def choose_pokemon(): #function for the user to choose a Pokemon
    print("Choose your character:")
    print("1. Pikachu")
    print("2. Bulbasaur")
    print("3. Jiglipuf")
    choice = input("Enter the number corresponding to the pokemon you want: ")
    
    if choice == "1":
        return pikachu
    elif choice == "2":
        return bulbasaur
    elif choice == "3":
        return jiglipuf
    else:
        print("Invalid selection. Defaulting to Pikachu.\n")
        return pikachu # by default


def choose_random_pokemon(): # function for the machine to choose a random Pokemon
    pokemons = [pikachu, bulbasaur, jiglipuf]
    random_pokemon = random.choice(pokemons)
    
    while random_pokemon == choose_pokemon():
        random_pokemon = random.choice(pokemons)
        
    return random_pokemon


# main game function
# it calls above func.
def play_game():  
    player_pokemon = choose_pokemon() 
    opponent_pokemon = choose_random_pokemon()
    
    print(f"You have selected {player_pokemon.name}!\n")
    print(f"The machine has selected {opponent_pokemon.name}!\n")

    # loop to continue game while both alive
    while player_pokemon.is_alive() and opponent_pokemon.is_alive():
        print()
        print("Your turn!\n")
        print("Attack skills:\n")
        print("1. Lightning\n")
        print("2. PoisonSeed\n")
        print("3. Chant\n")
        player_skill = input("Select an attack skill: ")
        
        lightning = AttackSkill("lightning", 25, 20) # instances skills
        poison_seed = AttackSkill("PoisonSeed", 20, 25)
        chant = AttackSkill("Chant", 20, 25)

        if player_skill == "1": # assigning skills
            skill = lightning
        elif player_skill == "2":
            skill = poison_seed
        elif player_skill == "3":
            skill = chant3
        else:
            print("Invalid choice. Please select a valid attack skill.\n")
            continue
        
        if not player_pokemon.has_enough_magic(skill.attack): ### verify magic
            print(player_pokemon.skills)
            print("STATUS", player_pokemon.magic)
            print("You don't have enough magic to use that skill. You lose your turn.\n")
        else:
            player_pokemon.attack(player_skill, opponent_pokemon)

        if opponent_pokemon.is_alive(): # verify if alive
            print()
            print("Machine's turn!\n")
            skills = [skill.attack for skill in opponent_pokemon.skills]
            if not skills:
                print("The machine doesn't have any attack skills. It loses its turn.\n")
                continue

            machine_skill = random.choice(skills)
            
            if not opponent_pokemon.has_enough_magic(machine_skill):
                print("The machine doesn't have enough magic to use that skill. It loses its turn.\n")
            else:
                opponent_pokemon.attack(machine_skill, player_pokemon)
        
    print()
    
    if player_pokemon.is_alive() and not opponent_pokemon.is_alive(): ###
        print(f"{player_pokemon.name} has won the battle!")
    elif opponent_pokemon.is_alive() and not player_pokemon.is_alive():
        print(f"{opponent_pokemon.name} has won the battle!")
    else:
        print("The battle ended in a draw.")
        
        
play_game()
