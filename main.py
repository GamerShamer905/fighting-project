from random import randint
class Minion:
    def __init__(self, name, health, attack_power, armour):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.armour = armour
    def die(self):
            return True
    def take_damage(self, amount):
        self.health = self.health - amount
        if self.health <= 0:
            self.die()
    def attack(self, target, attack):
        if randint(1, 100) == 1:
            crit_mult = 1.45
            print("CRITICAL HIT!")
        else:
             crit_mult = 1
        damage_amount = ((self.attack_power * attack.base_damage) * target.armour.defense_table[attack.attack_type])* crit_mult
        target.take_damage(damage_amount)
        print(f"You hit for {damage_amount}!")

class Attack:
    def __init__(self, attack_type, base_damage):
         self.attack_type = attack_type
         self.base_damage = base_damage

class Armour:
     def __init__(self, armour_type, defense_table):
            self.armour_type = armour_type
            self.defense_table = defense_table

leather = Armour(
    "Leather",
    {
         "slash":1.1,
         "pierce":1.25,
         "blunt":0.9,
         "magic":1
    }
)
plate = Armour(
    "Plate",
    {
         "slash":0.9,
         "pierce":1,
         "blunt":1.4,
         "magic":1
    }
)
chainmail = Armour(
    "Chainmail",
    {
         "slash":1,
         "pierce":1.3,
         "blunt":1,
         "magic":1
    }
)
katana_rush = Attack("slash", 1.1)
longsword_sweep = Attack("slash", 1.2)
dual_blade_fury = Attack("slash", 1.3)
whirlwind_cut = Attack("slash", 1.25)
rending_arc = Attack("slash", 1.4)
dagger_thrust = Attack("pierce", 1.0)
longspear_throw = Attack("pierce", 1.3)
needle_strike = Attack("pierce", 0.9)
assassin_stab = Attack("pierce", 1.35)
crossbow_puncture = Attack("pierce", 1.2)
warhammer_smash = Attack("blunt", 1.5)
shield_bash = Attack("blunt", 1.0)
fist_of_iron = Attack("blunt", 1.1)
ground_breaker = Attack("blunt", 1.45)
club_crash = Attack("blunt", 1.2)
fireball_burst = Attack("magic", 1.4)
ice_spear = Attack("magic", 1.2)
lightning_arc = Attack("magic", 1.6)
arcane_explosion = Attack("magic", 1.7)
shadow_bolt = Attack("magic", 1.3)

#character creation
player1_name = str(input("Input your characters name Player 1"))
player1_armour = str(input("What armour type do you want. Leather (L), Plate (P), Chainmail (C): "))
if player1_armour == "C":
    player1_armour = chainmail
elif player1_armour == "L":
    player1_armour = leather
elif player1_armour == "P":
    player1_armour = plate
else:
    print("invalid armour, defaulting to leather, womp womp")
    player1_armour = leather
print(f"YOU HAVE 20 POINTS, {player1_name}. YOU CAN INVEST INTO HEALTH AND DAMAGE")
player1_pointamount = 20
while True:
    player1_health_points = int(input("Enter the amount of points you would like to invest into health: "))
    if player1_health_points < 0:
        print("Cannot invest negative points")
    elif player1_health_points > player1_pointamount:
        print(f"You don't have enough points. You currently have {player1_pointamount} points.")
    else:
        player1_pointamount -= player1_health_points
        print(f"Health invested: {player1_health_points}")
        print(f"Remaining points: {player1_pointamount}")
        break

while True:
    player1_damage_points = int(input("Enter the amount of points you would like to invest into damage: "))
    if player1_damage_points < 0:
        print("Cannot invest negative points")
    elif player1_damage_points > player1_pointamount:
        print(f"You don't have enough points. You currently have {player1_pointamount} points.")
    else:
        player1_pointamount -= player1_damage_points
        print(f"Damage invested: {player1_damage_points}")
        print(f"Remaining points: {player1_pointamount}")
        if player1_pointamount > 0:
            remaining_points = str(input("Would you like to invest the rest into strength (S) or health (H)?: "))
            if remaining_points == "S":
                player1_damage_points = player1_damage_points + player1_pointamount
            if remaining_points == "H":
                player1_health_points = player1_health_points + player1_pointamount
        break

player1 = Minion(
    player1_name,
    player1_health_points * 15,
    player1_damage_points * 2,
    player1_armour
)



player2_name = str(input("Input your characters name Player 2"))
player2_armour = str(input("What armour type do you want. Leather (L), Plate (P), Chainmail (C): "))
if player2_armour == "C":
    player2_armour = chainmail
elif player2_armour == "L":
    player2_armour = leather
elif player2_armour == "P":
    player2_armour = plate
else:
    print("invalid armour, defaulting to leather, womp womp")
    player2_armour = leather
print(f"YOU HAVE 20 POINTS, {player2_name}. YOU CAN INVEST INTO HEALTH AND DAMAGE")
player2_pointamount = 20
while True:
    player2_health_points = int(input("Enter the amount of points you would like to invest into health: "))
    if player2_health_points < 0:
        print("Cannot invest negative points")
    elif player2_health_points > player2_pointamount:
        print(f"You don't have enough points. You currently have {player2_pointamount} points.")
    else:
        player2_pointamount -= player2_health_points
        print(f"Health invested: {player2_health_points}")
        print(f"Remaining points: {player2_pointamount}")
        break

while True:
    player2_damage_points = int(input("Enter the amount of points you would like to invest into damage: "))
    if player2_damage_points < 0:
        print("Cannot invest negative points")
    elif player2_damage_points > player2_pointamount:
        print(f"You don't have enough points. You currently have {player2_pointamount} points.")
    else:
        player2_pointamount -= player2_damage_points
        print(f"Damage invested: {player2_damage_points}")
        print(f"Remaining points: {player2_pointamount}")
        if player2_pointamount > 0:
            remaining_points = str(input("Would you like to invest the rest into strength (S) or health (H)?: "))
            if remaining_points == "S":
                player2_damage_points = player2_damage_points + player2_pointamount
            if remaining_points == "H":
                player2_health_points = player2_health_points + player2_pointamount
        break

player2 = Minion(
    player2_name,
    player2_health_points * 15,
    player2_damage_points * 2,
    player2_armour
)

attacks = [
    "Katana Rush",
    "Longsword Sweep",
    "Dual Blade Fury",
    "Whirlwind Cut",
    "Rending Arc",

    "Dagger Thrust",
    "Longspear Throw",
    "Needle Strike",
    "Assassin Stab",
    "Crossbow Puncture",

    "Warhammer Smash",
    "Shield Bash",
    "Fist of Iron",
    "Ground Breaker",
    "Club Crash",

    "Fireball Burst",
    "Ice Spear",
    "Lightning Arc",
    "Arcane Explosion",
    "Shadow Bolt"
]
def choose_attacks(attacks):
    while True:
        attack1 = randint(1, len(attacks))
        attack2 = randint(1, len(attacks))
        attack3 = randint(1, len(attacks))
        if attack1 == attack2 or attack1 == attack3 or attack2 == attack1 or attack2 == attack3:
            pass
        else:
            return [attack1, attack2, attack3]
