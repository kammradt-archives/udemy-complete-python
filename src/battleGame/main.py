from src.battleGame.classes.Person import Person


def main():
    spells = {
        'Fire Flame': {'cost': 10, 'damage': 50},
        'Fire Ball': {'cost': 15, 'damage': 60},
        'Thunder': {'cost': 20, 'damage': 75},
        'Lightning Spark': {'cost': 50, 'damage': 150}
    }

    person1 = Person(200, 100, 50, 50, spells)
    person1.print_spells()
    person1.choose_action()


if __name__ == '__main__':
    main()
