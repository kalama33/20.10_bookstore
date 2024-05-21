from pokemon import Pokemon, AttackSkill

def test_attack():
    pikachu = Pokemon("pikachu", 150, 220)
    bulbasaur = Pokemon("bulbasaur", 150, 220)

    lightning = AttackSkill("lightning", 25, 20)
    bombing = AttackSkill("poisonSeed", 20, 25)

    pikachu.learn_attack_skill(lightning)
    pikachu.learn_attack_skill(bombing)

    bulbasaur.learn_attack_skill(lightning)
    bulbasaur.learn_attack_skill(bombing)

    pikachu.attack(lightning.attack, bulbasaur)
    assert bulbasaur.health == 125

    bulbasaur.attack(lightning.attack, pikachu)
    assert pikachu.health == 125

    pikachu.attack(bombing.attack, bulbasaur)
    assert bulbasaur.health == 105