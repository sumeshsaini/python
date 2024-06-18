import random

class Player:
    def __init__(self, name, health, strength, attack):
        self.name = name
        self.health = health
        self.strength = strength
        self.attack = attack

    def is_alive(self):
        return self.health > 0

    def defend(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

class MagicalArena:
    def __init__(self, player_a, player_b):
        self.player_a = player_a
        self.player_b = player_b

    def roll_dice(self):
        return random.randint(1, 6)

    def attack(self, attacker, defender):
        input("Press Enter for next turn...")
        attack_roll = self.roll_dice()
        defense_roll = self.roll_dice()

        attack_damage = attacker.attack * attack_roll
        defense_strength = defender.strength * defense_roll

        damage_taken = max(attack_damage - defense_strength, 0)
        defender.defend(damage_taken)

        print(f"{attacker.name} attacks {defender.name} with roll {attack_roll}")
        print(f"{defender.name} defends with roll {defense_roll}")
        print(f"{defender.name}'s health reduced to {defender.health}")
        print("------------------------------")

    def battle(self):
        print("Let the battle begin!")
        print("------------------------------")
        while self.player_a.is_alive() and self.player_b.is_alive():
            self.attack(self.player_a, self.player_b)
            if self.player_b.is_alive():
                self.attack(self.player_b, self.player_a)

        if self.player_a.is_alive():
            print(f"{self.player_a.name} wins the battle!")
        else:
            print(f"{self.player_b.name} wins the battle!")

if __name__ == "__main__":
    name, health, strength, attack = input("Enter Player A details (name, health, strength, attack(use space for separation)): ").split()
    player_a = Player(name, int(health), int(strength), int(attack))

    name, health, strength, attack = input("Enter Player B details (name, health, strength, attack(use space for separation)): ").split()
    player_b = Player(name, int(health), int(strength), int(attack))

    arena = MagicalArena(player_a, player_b)
    arena.battle()
