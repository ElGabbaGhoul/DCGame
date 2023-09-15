class Hero:
    def __init__(self, name="Bujo"):
        self.name = name
        self.health = 100  # Initial health
        self.mana = 50     # Initial mana
        self.inventory = []
    
    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has been defeated.")
    
    def use_health_potion(self):
        if "health_potion" in self.inventory:
            self.health += 25 
            self.inventory.remove("health_potion")
            print(f"{self.name} used a health potion. Health: {self.health}")
        else:
            print(f"{self.name} doesn't have any health potions.")
    
    def add_item_to_inventory(self, item):
        self.inventory.append(item)
        print(f"{self.name} acquired {item}.")
    
    def cast_spell(self, spell_name):
        self.health = 50
        if spell_name == "fireball":
            if self.mana >= 20:
                self.mana -= 20
                print(f"{self.name} casts Fireball! Mana: {self.mana}.")
                # Target takes x damage, DoT
            else:
                print(f"{self.name} doesn't have enough mana to cast Fireball.")
        if spell_name == "heal":
            if self.mana >= 35:
                self.mana -= 35
                self.health += 30
                print(f"{self.name} casts Heal! Mana: {self.mana}. Health: {self.health}.")
            else:
                print(f"{self.name} doesn't have enough mana to cast Heal.")
        # if spell_name == "sleet":
        #     if self.mana >= 100:
        #         self.mana >= 100
        #         print(f"{self.name} casts Sleet! Mana: {self.mana}")
        #         # Target takes x damage, is stunned
        #     else:
        #         print(f"{self.name} doesn't have enough mana to cast Sleet.")

