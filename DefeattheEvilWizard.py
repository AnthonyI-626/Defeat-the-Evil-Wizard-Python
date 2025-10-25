import random

class Character:

    def __init__(self, name, health, attack_power):

        self.name = name

        self.health = health

        self.attack_power = attack_power

        self.max_health = health  
        
        self.is_blinded = False



    def attack(self, opponent):

        opponent.health -= self.attack_power

        print(f"--{self.name} attacks {opponent.name} for {self.attack_power} damage!")

        if opponent.health <= 0:

            print(f"--{opponent.name} has been defeated!")



    def display_stats(self):

        print(f"--{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")



# Warrior class (inherits from Character)

class Warrior(Character):

    def __init__(self, name):

        super().__init__(name, health=130, attack_power=20)  
        
    def war_cry(self, opponent):
        damage = random.randint(10, 25) * 2
        opponent.health -= damage
        print(f'--{self.name} uses War Cry to deal double damage! Damage dealt: {damage}!')
        
    def dampen_blow(self, damage):
        reduced_damage = damage // 2
        self.health -= reduced_damage
        print(f'--{self.name} uses Dampen Blow to reduce incoming damage by half!')
        
    def flask_of_fortitude(self):
        heal_amount = 20
        self.health = min(self.health + heal_amount, self.max_health)
        print(f'--{self.name} uses Flask of Fortitude to heal {heal_amount} health!')
            
        
        



# Mage class (inherits from Character)

class Mage(Character):

    def __init__(self, name):

        super().__init__(name, health=110, attack_power=30) 
    def flame_breath(self, opponent):
        damage = random.randint(25, 35)
        opponent.health -= damage
        print(f'--{self.name} uses Flame Breath to deal {damage} damage!')    
        
    def ice_spear(self, opponent):
        reduction = 15
        opponent.attack_debuff_turns = 1
        opponent.attack_power -= reduction
        print(f'--{self.name} uses Ice Spear to reduce {opponent.name}\'s attack power by {reduction}!')
        
    def healing_sigil(self):
        heal_amount = 35
        self.health = min(self.health + heal_amount, self.max_health)
        print(f'--{self.name} uses Healing Sigil to heal {heal_amount} health!')
        



# EvilWizard class (inherits from Character)

class EvilWizard(Character):

    def __init__(self, name):

        super().__init__(name, health=150, attack_power=20) 
        self.base_attack_power = self.attack_power
        self.black_sun_targets = {}
        self.attack_debuff_turns = 0
        
    def black_sun(self, opponent):
        duration = 3
        self.black_sun_targets[opponent] = duration
        print(f'--{self.name} uses Black Sun on {opponent.name} for {duration} turns!')
        
        
    
    def blood_drain(self, opponent):
        damage = 20
        opponent.health -= damage
        self.health = min(self.health + damage, self.max_health)
        print(f'--{self.name} uses Blood Drain to deal {damage} damage and heal for {damage} health!')
        
    def Lighting_ark(self,opponent):
        damage = 20
        opponent.health -= damage
        print(f'--{self.name} uses Lighting Ark to deal {damage} damage!')
        
    def shadow_bolt(self, opponent):
        damage = 20
        opponent.health -= damage
        print(f'--{self.name} uses Shadow Bolt to deal {damage} damage!')
        
        if random.random() < 0.25:
            opponent.is_blinded = True
            print(f'--{opponent.name} is blinded and will miss their next turn!')
            
    def regenerate(self):
        self.health = min(self.health + 5, self.max_health)
        print(f'--{self.name} regenerates 5 health! Current health is: {self.health}.')
        
        


# Create Rogue class

class Rogue(Character):
    def __init__(self, name):
        
        super().__init__(name,health=100,attack_power=10) 
    def quick_slash(self, opponent):
        damage = random.randint(15, 30)
        opponent.health -= damage
        print(f'--{self.name} uses Quick Slash to deal {damage} damage!')
        
    def piercing_arrow(self, opponent):
        damage = 35
        opponent.health -= damage
        print(f'--{self.name} uses Piercing Arrow to deal {damage} damage!')
        
    def flask_of_recovery(self):
        heal_amount = 30
        self.health = min(self.health + heal_amount, self.max_health)
        print(f'--{self.name} uses Flask of Recovery to heal {heal_amount} health!')
        
        



# Create Paladin class 

class Paladin(Character):
    def __init__(self, name):
        
        super().__init__(name,health=145,attack_power=25) 
        self.defense_turns = 0
        
        
    def divine_light(self):
        heal_amount = 25
        self.health = min(self.health + heal_amount, self.max_health)
        print(f'--{self.name} uses Divine Light to heal {heal_amount} health!')
        
    def bolstered_defense(self, damage):
        self.defense_turns = 2
        reduced_damage = damage // 3
        self.health -= reduced_damage
        print(f'--{self.name} uses Bolstered Defense to reduce incoming damage by two-thrids for 2 turns!')
        
    def vengeful_strike(self, opponent):
        damage = random.randint(20, 45) + 10
        opponent.health -= damage
        print(f'--{ self.name} uses Vengful Strike to deal {damage} damage!')
        
        
        
        
        
    



def create_character():

    print("--Choose your character class:")

    print("1. Warrior")

    print("2. Mage")

    print("3. Rogue") 

    print("4. Paladin")  



    class_choice = input("--Enter the number of your class choice: ")

    name = input("--Enter your character's name: ")



    if class_choice == '1':

        return Warrior(name)

    elif class_choice == '2':

        return Mage(name)

    elif class_choice == '3':

        return Rogue(name)

    elif class_choice == '4':

        return Paladin(name)

    else:

        print("--Invalid choice. Defaulting to Warrior.")

        return Warrior(name)



def battle(player, wizard):

    while wizard.health > 0 and player.health > 0:

        print("\n--- Your Turn ---")

        print("1. Attack")

        print("2. Use Special Ability")

        print("3. Heal")

        print("4. View Stats")



        choice = input("Choose an action: ")
        
        
        if player.is_blinded:
            print(f'--{player.name} is blinded and misses their turn!')
            player.is_blinded = False
            continue



        if choice == '1':

            if isinstance(player, Warrior):
                player.war_cry(wizard)
                
            elif isinstance(player, Mage):
                player.flame_breath(wizard)
                
            elif isinstance(player,Rogue):
                player.quick_slash(wizard)
                
            elif isinstance(player, Paladin):
                player.vengeful_strike(wizard)

        elif choice == '2':
            if isinstance(player, Warrior):
                player.dampen_blow(wizard.attack_power)
            
            elif isinstance(player, Mage):
                player.ice_spear(wizard)
                
            elif isinstance(player, Rogue):
                player.piercing_arrow(wizard)
                
            elif isinstance(player, Paladin):
                player.bolstered_defense(wizard.attack_power)

        elif choice == '3':

            if isinstance(player, Warrior):
                player.flask_of_fortitude()
            
            elif isinstance(player, Mage):
                player.healing_sigil()
            
            elif isinstance(player, Rogue):
                player.flask_of_recovery()
                
            elif isinstance(player, Paladin):
                player.divine_light()

        elif choice == '4':

            player.display_stats()

        else:

            print("Invalid choice. Try again.")
            
        if player in wizard.black_sun_targets:
            print(f'--{player.name} is affected by Black Sun and takes 5 damage!')
            player.health -= 5 
            wizard.black_sun_targets[player] -= 1
            
            if wizard.black_sun_targets[player] <= 0:
                del wizard.black_sun_targets[player]
                print(f'--{player.name} is no longer affected by Black Sun!')
                
            if player.health <= 0:
                print(f"--{player.name} has been defeated!")

                break
            



        if wizard.health > 0:
            
            if wizard.attack_debuff_turns > 0:
                wizard.attack_debuff_turns -= 1
                if wizard.attack_debuff_turns == 0:
                    wizard.attack_power = wizard.base_attack_power
                    

            wizard.regenerate()

            ability_choice = random.choice(['shadow_bolt', 'blood_drain', 'Lighting_ark', 'black_sun'])
            
            if ability_choice == 'shadow_bolt':
                wizard.shadow_bolt(player)
            elif ability_choice == 'blood_drain':
                wizard.blood_drain(player)
            elif ability_choice == 'Lighting_ark':
                wizard.Lighting_ark(player)
            elif ability_choice == 'black_sun':
                wizard.black_sun(player)
            
        if isinstance(player, Paladin) and player.defense_turns > 0:
            reduced_damage = wizard.attack_power // 3
            player.health -= reduced_damage
            player.defense_turns -= 1
            print(f'--{player.name}\'s Bolstered Defense reduces damage to {reduced_damage}.')



        if player.health <= 0:

            print(f"--{player.name} has been defeated!")

            break



    if wizard.health <= 0:

        print(f" --{wizard.name} has been defeated by {player.name}!")



def main():

    player = create_character()

    wizard = EvilWizard("The Dark Wizard")

    battle(player, wizard)



if __name__ == "__main__":

    main()