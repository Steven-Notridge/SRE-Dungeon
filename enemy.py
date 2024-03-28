import random

class Enemy:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has been defeated!")
        else:
            print(f"{self.name} loses {damage} hp. {self.name}'s remaining hp: {self.health}")

    def attack(self):
        attack_damage = random.randint(1, self.damage)
        print(f"{self.name} attacks you and deals {attack_damage} damage!")
        return attack_damage
