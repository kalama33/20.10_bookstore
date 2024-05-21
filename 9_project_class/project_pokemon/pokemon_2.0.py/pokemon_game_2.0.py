from pokemones import Pokemon, AttackSkill
import random
import os

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


def choose_random_pokemon(): # function for the machine to choose a random pokemon !=
    player_pokemon = choose_pokemon() 
    pokemons = [pikachu, bulbasaur, jiglipuf]
    pokemons.remove(player_pokemon) # remove user selection
    random_pokemon = random.choice(pokemons) # just 2 values
    
    return random_pokemon, player_pokemon # return bth as a tuple
    #print(choose_random_pokemon())


# main game logic
def play_game():
    
    opponent_pokemon, player_pokemon = choose_random_pokemon() # calling both inst.
    os.system("clear") # to clear 
    
    print(f"You have selected {player_pokemon.name}!\n")
    print(f"The machine has selected {opponent_pokemon.name}!\n")

    # player's turn as long they are alive
    while player_pokemon.is_alive() and opponent_pokemon.is_alive():
        print()
        print("Your turn!\n")
        print("Attack skills:\n")
        
        # user prompted to choose attack skill
        for i, skill in enumerate(player_pokemon.skills):
            print(f"{i+1}. {skill.attack}\n")
        player_skill = input("Select an attack skill: ")
        
        os.system("clear")
        
        # valid choice?
        if not player_skill.isdigit() or int(player_skill) < 1 or int(player_skill) > len(player_pokemon.skills):
            print("Invalid choice. Please select a valid attack skill.")
            continue
        
        # player input to an int. substract 1 to get the index of chosen attack
        skill_index = int(player_skill) - 1
        # variable that stores names o the attach skills
        skill_name = player_pokemon.skills[skill_index].attack

        # enough magic if it is, attack method
        if not player_pokemon.has_enough_magic(skill_name):
            print("You don't have enough magic to use that skill. You lose your turn.")
        else:
            player_pokemon.attack(skill_name, opponent_pokemon)

        if opponent_pokemon.is_alive():
            print()
            print("Machine's turn!\n")
            machine_skill = random.choice(opponent_pokemon.skills).attack

            if not opponent_pokemon.has_enough_magic(machine_skill):
                print("The machine doesn't have enough magic to use that skill. It loses its turn.")
            else:
                opponent_pokemon.attack(machine_skill, player_pokemon)

    print()
    if player_pokemon.is_alive():
        print(f"{player_pokemon.name} has won the battle!")
    elif opponent_pokemon.is_alive():
        print(f"{opponent_pokemon.name} has won the battle!")
    else:
        print("The battle ended in a draw.")

play_game()