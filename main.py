from random import randint, sample
class Minion:
    def __init__(self, name, health, attack_power, armour):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.armour = armour
    def die(self):
            print(f"{self.name} has DIED.")
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
    def __init__(self, name, attack_type, base_damage):
         self.name = name
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
katana_rush = Attack("Katana Rush", "slash", 1.1)
longsword_sweep = Attack("Longsword Sweep", "slash", 1.2)v
dual_blade_fury = Attack("Dual Blade Fury", "slash", 1.3)i
whirlwind_cut = Attack("Whirlwind Cut", "slash", 1.25)h
rending_arc = Attack("Rending Arc", "slash", 1.4)a
dagger_thrust = Attack("Dagger Thrust", "pierce", 1.0)a
longspear_throw = Attack("Longspear Throw", "pierce", 1.3)n
needle_strike = Attack("Needle Strike","pierce", 0.9)
assassin_stab = Attack("Assassin Stab", "pierce", 1.35)
crossbow_puncture = Attack("Crossbow","pierce", 1.2)
warhammer_smash = Attack("Warhammer Smash", "blunt", 1.5)
shield_bash = Attack("Shield Bash", "blunt", 1.0)
fist_of_iron = Attack("Fist of Iron", "blunt", 1.1)
ground_breaker = Attack("Ground Breaker", "blunt", 1.45)
club_crash = Attack("Club Crash", "blunt", 1.2)
fireball_burst = Attack("Fireball Burst", "magic", 1.4)
ice_spear = Attack("Ice Spear","magic", 1.2)
lightning_arc = Attack("Lightning Arc", "magic", 1.6)
arcane_explosion = Attack("Arcane Explosion", "magic", 1.7)
shadow_bolt = Attack("Shadow Bolt", "magic", 1.3)

#character creation
player1_name = str(input("Input your characters name Player 1: "))
player1_armour = str(input("What armour type do you want. Leather (L), Plate (P), Chainmail (C): "))
if player1_armour == "C":
    player1_armour = chainmail
elif player1_armour == "L":
    player1_armour = leather
elif player1_armour == "P":
    player1_armour = plate
else:
    print("invalid armour, defaulting to leather")
    player1_armour = leather
print(f"YOU HAVE 20 POINTS, {player1_name}. YOU CAN INVEST INTO HEALTH AND DAMAGE")
player1_pointamount = 20
while True:
    player1_health_points = int(input("Enter the amount of points you would like to invest into health: "))
    if player1_health_points < 0:
        print("Cannot invest negative points")
    elif player1_health_points > player1_pointamount:
        print(f"You don't have enough points. You currently have {player1_pointamount} points.")
    elif player1_health_points == 0:
        print("Health invested: 0")
        print(f"Remaining points: {player1_pointamount}")
        break
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



player2_name = str(input("Input your characters name Player 2: "))
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
    katana_rush,
    longsword_sweep,
    dual_blade_fury,
    whirlwind_cut,
    rending_arc,

    dagger_thrust,
    longspear_throw,
    needle_strike,
    assassin_stab,
    crossbow_puncture,

    warhammer_smash,
    shield_bash,
    fist_of_iron,
    ground_breaker,
    club_crash,

    fireball_burst,
    ice_spear,
    lightning_arc,
    arcane_explosion,
    shadow_bolt
]
def choose_attacks(attacks):
    random = sample(attacks, 3)
    return random

def check_winner(player1, player2):
    if player1.health <= 0:
        return player2.name
    elif player2.health <= 0:
        return player1.name
    return None
        
def play(player1, player2, attacks):
    print("PLAYER 1 STARTS")
    while True:
        player1_attacks = choose_attacks(attacks)
        print(f"Your attack options are: \n 1. {player1_attacks[0].name} \n 2. {player1_attacks[1].name} \n 3. {player1_attacks[2].name}")
        player1_chosen_attack = int(input("Which attack do you choose?: "))
        player1.attack(player2, player1_attacks[player1_chosen_attack-1])
        print(f"HEALTH: {player1.health}")
        winner = check_winner(player1, player2)
        if winner:
            break

        player2_attacks = choose_attacks(attacks)
        print(f"Your attack options are: \n 1. {player2_attacks[0].name} \n 2. {player2_attacks[1].name} \n 3. {player2_attacks[2].name}")
        player2_chosen_attack = int(input("Which attack do you choose?: "))
        player2.attack(player1, player2_attacks[player2_chosen_attack-1])
        print(f"HEALTH: {player2.health}")
        winner = check_winner(player1, player2)
        if winner:
            break
    winner = check_winner(player1, player2)
    print(f"{winner} Won!")


































play(player1, player2, attacks)