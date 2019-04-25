import random


class Person:

    def __init__(self, hp, mp, atk, defense, spells):
        self.hp = hp
        self.max_hp = hp
        self.mp = mp
        self.max_mp = mp
        self.min_atk = atk - 10
        self.max_atk = atk + 10
        self.defense = defense
        self.spells = spells
        self.actions = ['Attack', 'Magic']

    def get_hp(self):
        return self.hp

    def reduce_hp(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def get_max_hp(self):
        return self.max_hp

    def get_mp(self):
        return self.mp

    def reduce_mp(self, cost):
        self.mp -= cost

    def get_max_mp(self):
        return self.max_mp

    def get_attack_damage(self):
        return random.randrange(self.min_atk, self.max_atk)

    def print_spells(self):
        print('Your avaible spells are: ')
        for name in self.spells.keys():
            if self.has_enough_mp(self.get_spell_cost(name)):
                print('Spell name: {}, cost: {}.'.format(name, self.get_spell_cost(name)))

    def has_enough_mp(self, cost):
        return self.mp >= cost

    def get_spell_cost(self, spell_name):
        return self.spells.get(spell_name).get('cost')

    def get_spell_damage(self, spell_name):
        spell_damage = self.spells.get(spell_name).get('damage')

        spell_min_damage = spell_damage - 5
        spell_max_damage = spell_damage + 5
        return random.randrange(spell_min_damage, spell_max_damage)

    def choose_action(self):
        for i, option in enumerate(self.actions):
            print('{}: {}'.format(str(i), option))

