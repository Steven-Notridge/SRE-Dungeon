import random


# Class
class Player:
    def __init__(self, name, level, ctype, max_hp, current_health, base_damage, strength, defence, intelligence, vitality, dexterity, crit_chance, xp, xp_stage):
        self.name = name
        self.level = level
        self.ctype = ctype
        self.max_hp = max_hp
        self.current_health = current_health
        self.base_damage = base_damage
        self.strength = strength
        self.defence = defence
        self.intelligence = intelligence
        self.dexterity = dexterity
        self.crit_chance = crit_chance
        self.vitality = vitality
        self.xp = xp
        self.xp_stage = xp_stage
        self.next_stage_xp = 1000

    def take_damage(self, damage):
        self.current_health -= damage
        if self.current_health <= 0:
            print("You have been defeated. Game Over!")
        else:
            print(f"You take {damage} damage! Your remaining hp: {self.current_health} / {self.max_hp}")

    # def crit(self):
    #     crit_roll = random.randint(1, 6)
    #     print(f"crit roll: {crit_roll}")
    #     if crit_roll <= self.crit_chance:
    #         return True, crit_roll
    #     else:
    #         return False, crit_roll

    # def attack(self):
    #     print("inside attack")
    #     print(f"crit roll: {self.crit}")
    #     if self.crit:
    #         attack_damage = random.randint(1, self.base_damage)
    #         crit_attack = attack_damage * 2
    #         return crit_attack
    #     else:
    #         attack_damage = random.randint(1, self.base_damage)
    #         print(f"You attack and deal {attack_damage} damage!")
    #         return attack_damage

    def attack(self):
        attack_damage = self.base_damage
        crit_roll = random.randint(1, 10)  # Generate a random number between 1 and 10
        if crit_roll <= self.crit_chance:  # If the roll is less than or equal to the crit chance
            crit_attack = attack_damage * 2  # Double the damage
            print("Critical hit!")
            return crit_attack
        else:
            print(f"You attack and deal {attack_damage} damage!")
            return attack_damage

    def level_up(self, stages):
        if self.xp_stage < len(stages) and self.xp >= stages[self.xp_stage]:
            self.next_stage_xp = stages[self.xp_stage] if self.xp_stage + 1 == len(stages) else stages[self.xp_stage + 1]
            print(f"Congratulations! You have reached Level {self.xp_stage + 1}.")
            if self.xp_stage < len(stages) - 1:
                print(f"Required XP for next stage: {self.next_stage_xp}")
            self.xp_stage += 1
            self.xp = 0
            return True, self.next_stage_xp
        else:
            print(f"Required XP till next level: {self.next_stage_xp}")
            return False

    def increase_stat(self, stat):
        if self.level_up:
            if hasattr(self, stat):
                setattr(self, stat, getattr(self, stat) + 1)
                if stat == 'strength':
                    self.base_damage += 1
                if stat == 'vitality':
                    self.max_hp += 1
                    print(f"You now have a max health pool of {self.max_hp}")
                print(f"{stat.capitalize()} has been increased by 1.")
                print(f"Your HP has been fully healed!")
                self.current_health = self.max_hp
                self.level += 1
                return self

        else:
            print(f"Invalid stat: {stat}. Please choose a valid stat.")
            return self


