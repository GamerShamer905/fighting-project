from random import randint
class Minion:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
    def die(self):
            return True
    def take_damage(self, amount):
        self.health = self.health - amount
        if self.health <= 0:
            self.die()
    def attack(self, target, attack, armour):
        if randint(1, 100) == 1:
            crit_mult = 1.45
            print("CRITICAL HIT!")
        else:
             crit_mult = 1
        target.take_damage(((self.attack_power * attack.base_damage) * armour.defense_table[attack.attack_type])* crit_mult)

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
print("YOU HAVE 20 POINTS. YOU CAN INVEST INTO HEALTH AND DAMAGE")
player1_pointamount = 20
health_points = int(input("Enter the amount of points you would like to invest into health: "))
if health_points < 0:
     print("")
player1()