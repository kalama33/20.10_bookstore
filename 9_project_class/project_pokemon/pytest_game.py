from pokemon import Pokemon, AttackSkill
import random
import pytest


# def test_play_game():
    

def test_battle():
    pikachu = Pokemon("pikachu", 150, 220)
    bulbasaur = Pokemon("bulbasaur", 150, 220)

    lightning = AttackSkill("lightning", 25, 20)
    bombing = AttackSkill("poisonSeed", 20, 25)

    pikachu.learn_attack_skill(lightning)
    pikachu.learn_attack_skill(bombing)

    bulbasaur.learn_attack_skill(lightning)
    bulbasaur.learn_attack_skill(bombing)

    #  battle sould end in a draw
    assert play_game(pikachu, bulbasaur) == "The battle ended in a draw."

    # pikachu should win the battle
    assert play_game(pikachu, bulbasaur) == "pikachu has won the battle!"

    # bulbasaur should win the battle
    assert play_game(pikachu, bulbasaur) == "bulbasaur has won the battle!"