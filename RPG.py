import random
import time

# Player and Monster class
class Character:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def take_damage(self, damage):
        self.health -= max(damage - self.defense, 0)

    def is_alive(self):
        return self.health > 0

    def attack_enemy(self, enemy):
        damage = random.randint(self.attack - 2, self.attack + 2)
        print(f"{self.name} attacks {enemy.name} for {damage} damage!")
        enemy.take_damage(damage)

    def heal(self):
        heal_amount = random.randint(5, 10)
        self.health += heal_amount
        print(f"{self.name} heals for {heal_amount} health!")

# Game logic
def start_game():
    print("Welcome to the simple RPG game!")
    time.sleep(1)

    player_name = input("Enter your character's name: ")
    player = Character(player_name, 100, 20, 5)
    monster = Character("Goblin", 80, 15, 3)

    while player.is_alive() and monster.is_alive():
        print("\nPlayer Health:", player.health)
        print("Monster Health:", monster.health)
        print("\nWhat do you want to do?")
        print("1. Attack")
        print("2. Heal")
        choice = input("Choose 1 or 2: ")

        if choice == "1":
            player.attack_enemy(monster)
        elif choice == "2":
            player.heal()
        else:
            print("Invalid choice! You do nothing.")
        
        if monster.is_alive():
            print("\nThe monster's turn!")
            monster.attack_enemy(player)
        
        time.sleep(1)

    if player.is_alive():
        print(f"\nCongratulations, {player.name}! You defeated the monster!")
    else:
        print(f"\nSorry, {player.name}, you were defeated by the monster.")

# Start the game
if __name__ == "__main__":
    start_game()
