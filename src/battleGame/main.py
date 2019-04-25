from src.battleGame.classes.Person import Person
from src.battleGame.classes.BackgroundColors import BackgroundColors as bg


def main():
    spells = {
        'Fire Flame': {'cost': 10, 'damage': 80},
        'Fire Ball': {'cost': 15, 'damage': 100},
        'Thunder': {'cost': 20, 'damage': 120},
        'Lightning Spark': {'cost': 50, 'damage': 250}
    }

    person1 = Person(200, 100, 50, 50, spells)
    enemy = Person(200, 100, 50, 50, spells)

    running = True
    while running:
        print('-' * 99)
        person1.choose_action()
        choice_action = int(input('Choose your action!: '))
        print('You chose: ', 'Attack!' if choice_action is 0 else 'Magic attack!')

        if choice_action is 0:
            person_damage = person1.get_attack_damage()
            enemy.reduce_hp(person_damage)
            print(bg.OKBLUE, 'Damage dealt:', person_damage, 'Enemy HP:', enemy.get_hp(), '/', enemy.get_max_hp(), bg.FAIL)

        else:
            person1.print_spells()
            choice_spell = input('Choose your magic attack!: \n')

            spell_damage = person1.get_spell_damage(choice_spell)
            enemy.reduce_hp(spell_damage)
            print(bg.OKBLUE, 'Player current MP:', person1.get_mp(), '/', person1.get_max_mp(), bg.ENDC)
            print(bg.OKBLUE, 'Damage dealt:', spell_damage, 'Enemy HP:', enemy.get_hp(), bg.ENDC)

        enemy_attacking(enemy, person1)

        if enemy.get_hp() is 0:
            print(bg.OKGREEN, 'Victory!', bg.ENDC)
            running = False
        elif person1.get_hp() is 0:
            print(bg.FAIL, 'You lose!', bg.ENDC)
            running = False


def enemy_attacking(enemy, person1):
    enemy_damage = enemy.get_attack_damage()
    person1.reduce_hp(enemy_damage)
    print(bg.FAIL, 'Damage dealt by enemy:', enemy_damage, 'Player HP:', person1.get_hp(), '/', person1.get_max_hp(), bg.ENDC)


if __name__ == '__main__':
    main()
