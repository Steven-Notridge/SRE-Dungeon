import json
import random
import os

from enemy import Enemy
from player import Player

# Read JSON data from external file
with open('data/enemies.json') as enemyjson:
    enemy_data = json.load(enemyjson)


player = Player("Hero", 0, "Warrior", 10, 10, 3, 0, 0, 0, 0, 0, 5, 0, 0)

xp_stages = [1000, 10000, 20, 40, 80]  # Define XP stages


class Game:
    def __init__(self):
        self.fight_round = 1  # Initialize round counter
        self.end_round = False

        # Get a random enemy from the JSON.
        self.enemy_name = random.choice(list(enemy_data.keys()))

        # Get the attributes of the randomly selected enemy
        self.enemy_health = enemy_data[self.enemy_name]["Health"]
        self.enemy_damage = enemy_data[self.enemy_name]["Damage"]

        # Create an instance of the Enemy class with the randomly selected attributes
        self.random_enemy = Enemy(self.enemy_name, self.enemy_health, self.enemy_damage)

    def reset_round(self):
        print("resetting round")
        # Get a random enemy from the JSON.
        self.enemy_name = random.choice(list(enemy_data.keys()))

        # Get the attributes of the randomly selected enemy
        self.enemy_health = enemy_data[self.enemy_name]["Health"]
        self.enemy_damage = enemy_data[self.enemy_name]["Damage"]

        # Create an instance of the Enemy class with the randomly selected attributes
        self.random_enemy = Enemy(self.enemy_name, self.enemy_health, self.enemy_damage)


    def user_interface(self):
        print(f"\n----- Round {self.fight_round} -----")
        print("You encounter an enemy!")
        print(f"A {self.enemy_name} appears!")
        print(f"Your HP: {player.current_health}/{player.max_hp}")

    def fight_start(self):
        global player
        while not self.end_round:
            print("Not self.end_round")

            # Clear screen - broken
            os.system('cls' if os.name == 'nt' else 'clear')

            self.user_interface()

            while self.random_enemy.health > 0 and player.current_health > 0:
                action = input("What will you do? (attack/stats/kill/quit) ").lower()

                if action == "attack":
                    player_damage = player.attack()
                    if self.random_enemy.health > 0:
                        # Random enemy takes damage based on (player_damage)
                        self.random_enemy.take_damage(player_damage)
                        if self.enemy_health > 0:
                            enemy_damage = self.random_enemy.attack()
                            player.take_damage(enemy_damage)

                elif action == "stats":
                    print(f"{player.name} the Level {player.level} {player.ctype} ")
                    print(f"Current Health: {player.current_health}/{player.max_hp}")
                    print(f"Strength: {player.strength}")
                    print(f"Damage: {player.base_damage}")
                    print(f"Defence: {player.defence}")
                    print(f"Intelligence: {player.intelligence}")
                    print(f"Dexterity: {player.dexterity}")
                    print(f"Critical Strike Chance: {player.crit_chance}")
                    print(f"Vitality: {player.vitality}")
                    print(f"Experience: {player.xp}/{player.next_stage_xp}")

                elif action == "kill":
                    print("You cheater.")
                    break

                elif action == "quit":
                    exit()

                else:
                    print("Invalid action. Please choose 'attack', 'stats' or 'flee'.")

            if player.current_health > 0 and not self.end_round:
                print("You defeated all enemies. You are victorious!")
                xp_gain = random.randint(1, 10)
                player.xp += xp_gain
                print(f"You have gained xp: {xp_gain}")
                self.fight_round += 1

            if player.level_up(xp_stages):
                print("Choose a stat to increase: (strength, defence, intelligence, vitality, dexterity)")
                stat_has_been_chosen = False
                while not stat_has_been_chosen:
                    chosen_stat = input().strip().lower()
                    if chosen_stat in ["strength", "defence", "intelligence", "vitality", "dexterity"]:
                        # Below references the chosen_stat and passes this to the increase_stat variable in Player
                        player = player.increase_stat(chosen_stat)
                        print("Updated player stats:")
                        print("Name:", player.name)
                        print("Type:", player.ctype)
                        print("Health:", player.current_health, "/", player.max_hp)
                        print("Base Damage:", player.base_damage)
                        print("Critical Strike Chance:", player.crit_chance)
                        print("Strength:", player.strength)
                        print("Defence:", player.defence)
                        print("Intelligence:", player.intelligence)
                        print("Vitality:", player.vitality)
                        print("Dexterity:", player.dexterity)
                        print("XP:", player.xp)
                        stat_has_been_chosen = True
                    else:
                        print("Invalid stat. Please choose a valid stat.")

            # Ask the player if they want to continue to the next round
            next_round = input("Do you want to continue to the next round? (yes/no) ").lower()
            if next_round == "yes":
                self.end_round = False
                self.reset_round()

            # To be used later for shops etc.
            if next_round == "no":
                self.end_round = True
