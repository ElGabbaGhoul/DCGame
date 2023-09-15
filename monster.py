import random

class Monster:
    def __init__(self, level):
        self.level = level
        self.prefix_ranges = {
            (1, 5): ["Tiny", "Non-Threatening", "Basic", "Wimpy", "Ankle-Biting"],
            (6, 10): ["Average", "Adolescent", "Goofy-Lookin'", "Face-Punching"],
            (11, 20): ["Lumbering", "Hulking", "Beefy", "Red-Eyed"],
            (21, 30): ["Towering", "Terrifying", "Bloodsoaked", "Powerful"],
            (31, 40): ["Giant", "Nightmarish", "Deadly", "Arcane"],
            (41, 50): ["Gargantuan", "Eldritch", "Lethal", "Legendary"]
        }
        self.monster_race = {
            # Each floor has one type of each race. Races: Gnorks, Serpentix, Arcanari, Dwarvorg, Eltharion, Varkin
            (1, 5): ["Gnublin", "Tinyfang", "Spellspark", "Stoneshield", "Willowkin", "Shadowling"],
            (6, 10): ["Knuckler", "Venomblade", "Manaflame", "Ironhammer", "Sylvanblade", "Bloodhunter"],
            (11, 20): ["Runetusk", "Viperspell", "Stormweaver", "Runeblade", "Erdstalker", "Necromancer"],
            (21, 30): ["Stoneguard", "Scalewarden", "Battlesage", "Earthbreaker", "Starwhisperer", "Dreadnaught"],
            (31, 40): ["Thunderlord", "Serpentlord", "Archmage", "Greatwarden", "Forestlord", "Soulshifter"],
            (41, 50): ["Grand Goliath", "Venomous Sovereign", "Arcane Archon", "Stoneforged Titan", "Ethereal Sentinel", "Faceless Voidreaver"]
        }
        self.prefix = self.get_random_prefix()
        self.race = self.get_random_race()
        self.monster_type = f"{self.prefix} {self.race}"
        self.health = self.calculate_health()
        self.is_boss = False

    def get_random_prefix(self):
        for level_range, prefixes in self.prefix_ranges.items():
            if level_range[0] <= self.level <= level_range[1]:
                return random.choice(prefixes)
        return "Unknown Prefix"

    def get_random_race(self):
        for level_range, races in self.monster_race.items():
            if level_range[0] <= self.level <= level_range[1]:
                return random.choice(races)
        return "Unknown Race"

    def calculate_health(self):
        base_health = 20
        for level_range, _ in self.prefix_ranges.items():
          if self.level == level_range[1]:
            level_health = round(((level_range[1] / level_range[0]) * self.level))
            return (base_health + level_health) * 2
          else:
            if level_range[0] <= self.level <= level_range[1]:
              level_health = round(((level_range[1] / level_range[0]) * self.level))
              return base_health + level_health


    def generate_monster(self):
        for level_range, _ in self.prefix_ranges.items():
            if level_range[0] <= self.level <= level_range[1]:
                if self.level == level_range[1]:
                    self.is_boss = True
                    boss_prefix = "BOSS"
                    self.monster_type = f"{boss_prefix} {self.monster_type}"
        return self.monster_type, self.health

level = random.randint(1, 50)
monster_instance = Monster(level)
monster, health = monster_instance.generate_monster()

print(f"Level {level}! You encounter {monster}! HP: {health}")
