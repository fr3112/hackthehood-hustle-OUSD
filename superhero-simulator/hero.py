#Lab 6 - Erika Ramos

from ability import Ability
from armor import Armor

import random
class Hero:
    def __init__(self, name, starting_health=100):
        '''Initialize Hero with a name and health values'''
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []
        self.armors = []

    def battle(self, opponent):
        '''Fight another hero and randomly declare a winner'''
        self.opponent = opponent
        
        print(f"{self.name} battles {opponent.name}!")

        #randomly choose a winner
        winner = random.choice([self.name, opponent.name])

        print(f"{winner} wins the battle")

    def add_ability(self, ability):
        self.abilities.append(ability)
        print(f"{ability.name} has been added to {self.name}'s")

    def sum_of_attacks(self):
        '''Loops through abilitiees list and sums up all'''
        total_damage = 0
        for  ability in self.abilities:
            total_damage += ability.attack()
        return total_damage
    
    def add_armor(self,armor):
        '''Adds an armor to the  armors list'''
        self.armors.append(armor)
        print(f"{armor.name} has been added to {self.name}'s")

    def defend(self):
        '''Loops through armors lists and  sums up all block value'''
        total_block = 0
        for armor in self.armors:
            total_block +=  armor.block()
        return total_block
      
if __name__ == "__main__":
    my_hero = Hero("Black Panther", 200)
    name1 = my_hero.name
    print(name1)            
    current_health1 = my_hero.current_health
    print(current_health1)

    my_hero2 = Hero("Spiderman", 200)
    name2 = my_hero2.name
    print(name2)            
    current_health2 = my_hero2.current_health
    print(current_health2)

    my_hero.battle(my_hero2)

    fireball =  Ability("Fireball", 50)
    lightning = Ability("Ligtning", 55)
    telekinesis = Ability("Telekinesis", 60)
    my_hero.add_ability(fireball)
    my_hero.add_ability(lightning)
    my_hero.add_ability(telekinesis)

    print(my_hero.sum_of_attacks())

    shield = Armor("Shield", 30)
    helmet = Armor ("Helmet", 25)
    boots = Armor("Boots", 10)
    my_hero.add_armor(shield)
    my_hero.add_armor(helmet)
    my_hero.add_armor(boots)

    print(my_hero.defend())

    

