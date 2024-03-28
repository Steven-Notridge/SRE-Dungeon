import random
import json

# Read JSON data from external file
with open('data/enemies.json') as json_file:
    enemy_data = json.load(json_file)


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

player = Player("Hero", "Warrior", 10, 10, 3, 0, 0, 0, 0, 0, 0)

def main():
    global player
    fight_round = 1  # Initialize round counter
    end_game = False  # Flag to track if the game should end

    while not end_game:
        # Get a random enemy from the JSON.
        enemy_name = random.choice(list(enemy_data.keys()))

        # Get the attributes of the randomly selected enemy
        enemy_health = enemy_data[enemy_name]["Health"]
        enemy_damage = enemy_data[enemy_name]["Damage"]

        # Create an instance of the Enemy class with the randomly selected attributes
        random_enemy = Enemy(enemy_name, enemy_health, enemy_damage)

        # player_stats = {'strength': 0, 'defence': 0, 'intelligence': 0, 'vitality': 0, 'dexterity': 0}  # Player's stats

        print(f"\n----- Round {fight_round} -----")
        print("You encounter an enemy!")
        print(f"A {enemy_name} appears!")

        while random_enemy.health > 0 and player.current_health > 0:
            action = input("What will you do? (attack/stats/flee) ").lower()

            if action == "attack":
                player_damage = player.base_damage
                if random_enemy.health > 0:
                    # Random enemy takes damage based on (player_damage)
                    random_enemy.take_damage(player_damage)
                    if enemy_health > 0:
                        enemy_damage = random_enemy.attack()
                        player.take_damage(enemy_damage)

            elif action == "stats":
                print(f"Current Health: {player.current_health}/{player.max_hp}")
                print(f"Strength: {player.strength}")
                print(f"Damage: {player.base_damage}")
                print(f"Defence: {player.defence}")
                print(f"Intelligence: {player.intelligence}")
                print(f"Dexterity: {player.dexterity}")
                print(f"Vitality: {player.vitality}")
                print(f"Experience: {player.xp}")

            elif action == "flee":
                print("You run away from the enemies!")
                break

            else:
                print("Invalid action. Please choose 'attack', 'stats' or 'flee'.")

        if player.current_health > 0 and not end_game:
            print("You defeated all enemies. You are victorious!")
            xp_gain = random.randint(1, 10)
            player.xp += xp_gain
            print(f"You have gained {xp_gain} experience points!")
            print(f"You have a total of {player.xp} experience points.")
            fight_round += 1

        if player.level_up(xp_stages):
            print("Choose a stat to increase: (strength, defence, intelligence, vitality, dexterity)")
            chosen_stat = input().strip().lower()
            player = player.increase_stat(chosen_stat)
            print("Updated player stats:")
            print("Name:", player.name)
            print("Type:", player.type)
            print("Health:", player.current_health, "/", player.max_hp)
            print("Base Damage:", player.base_damage)
            print("Strength:", player.strength)
            print("Defence:", player.defence)
            print("Intelligence:", player.intelligence)
            print("Vitality:", player.vitality)
            print("Dexterity:", player.dexterity)
            print("XP:", player.xp)

        # Ask the player if they want to continue to the next round
        next_round = input("Do you want to continue to the next round? (yes/no) ").lower()
        if next_round != "yes":
            end_game = True

xp_stages = [5, 10, 20, 40, 80]  # Define XP stages
if __name__ == "__main__":
    main()
