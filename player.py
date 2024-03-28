import random


# Class
class Player:
    def __init__(self, name, type, max_hp, current_health, base_damage, strength, defence, intelligence, vitality, dexterity, xp):
        self.name = name
        self.type = type
        self.max_hp = max_hp
        self.current_health = current_health
        self.base_damage = base_damage
        self.strength = strength
        self.defence = defence
        self.intelligence = intelligence
        self.dexterity = dexterity
        self.vitality = vitality
        self.xp = xp

    def take_damage(self, damage):
        self.current_health -= damage
        if self.current_health <= 0:
            print("You have been defeated. Game Over!")
        else:
            print(f"You take {damage} damage! Your remaining hp: {self.current_health} / {self.max_hp}")

    def attack(self, damage):
        attack_damage = random.randint(1, self.base_damage)
        print(f"You attack and deal {attack_damage} damage!")
        return attack_damage

    def level_up(self, stages):
        for stage, required_xp in enumerate(stages):
            if self.xp >= required_xp:
                print(f"Congratulations! You have reached stage {stage + 1}.")
                return True
        print("You haven't gained enough XP to level up yet.")
        return False

    def increase_stat(self, stat):
        if hasattr(self, stat):
            setattr(self, stat, getattr(self, stat) + 1)
            if stat == 'strength':
                self.base_damage += 1
            if stat == 'vitality':
                self.max_hp += 1
                print(f"You now have a max health pool of {player.max_hp}")
            print(f"{stat.capitalize()} has been increased by 1.")
            print(f"Your HP has been fully healed!")
            self.current_health = self.max_hp
            return self

        else:
            print(f"Invalid stat: {stat}. Please choose a valid stat.")
            return self


