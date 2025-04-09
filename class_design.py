import random

class Superhero:
    def __init__(self, name=None, secret_identity=None, power_source=None):
        self._name = name or self._generate_name()
        self.__secret_identity = secret_identity or self._generate_identity()
        self.power_source = power_source or self._generate_power_source()
        self.powers = self._generate_powers()
        self.catchphrase = self._generate_catchphrase()
        
    def _generate_name(self):
        prefixes = ["Captain", "Doctor", "The", "Super", "Ultra", "Mega"]
        suffixes = ["Strike", "Blast", "Wonder", "Power", "Storm", "Light"]
        return f"{random.choice(prefixes)} {random.choice(suffixes)}"
    
    def _generate_identity(self):
        first_names = ["Alex", "Jordan", "Taylor", "Casey", "Riley", "Jamie"]
        last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia"]
        return f"{random.choice(first_names)} {random.choice(last_names)}"
    
    def _generate_power_source(self):
        sources = ["Cosmic Energy", "Alien Technology", "Magical Artifact", 
                  "Genetic Mutation", "Ancient Training", "Scientific Accident"]
        return random.choice(sources)
    
    def _generate_powers(self):
        power_types = ["Elemental", "Physical", "Mental", "Energy", "Cosmic"]
        return {
            "type": random.choice(power_types),
            "strength": random.randint(1, 10),
            "unique_ability": random.choice(["Flight", "Invisibility", "Telekinesis", 
                                           "Shapeshifting", "Time Manipulation"])
        }
    
    def _generate_catchphrase(self):
        phrases = [
            "Justice tastes like strawberries!",
            "Your evil ends with a BANG!",
            "I fight for cupcakes and freedom!",
            "The night is dark but my spandex is bright!",
            "Evil-doers beware - the snacc is here!"
        ]
        return random.choice(phrases)
    
    def reveal_secret(self):
        return f"Shhh... I'm actually {self.__secret_identity}!"
    
    def __str__(self):
        return (f"🦸 {self._name}\n"
                f"Power Source: {self.power_source}\n"
                f"Powers: {self.powers['type']} (Strength: {self.powers['strength']}/10)\n"
                f"Special Ability: {self.powers['unique_ability']}\n"
                f"Catchphrase: '{self.catchphrase}'")

def main():
    print("🌟 SUPERHERO CREATOR 🌟")
    print("Create your own superhero!\n")
    
    # Get user input or use random generation
    choice = input("Would you like to:\n1. Create a custom hero\n2. Generate a random hero\n> ")
    
    if choice == "1":
        name = input("Enter hero name: ")
        identity = input("Enter secret identity: ")
        power_source = input("Enter power source: ")
        hero = Superhero(name, identity, power_source)
    else:
        hero = Superhero()
        print("\nGenerating a random superhero...")
    
    print("\n✨ YOUR SUPERHERO ✨")
    print(hero)
    print(hero.reveal_secret())
    
    # Team creation demo
    print("\nLet's create a team!")
    team_name = input("Enter team name: ")
    team_size = int(input("How many heroes on your team? (2-4): "))
    
    team = []
    for i in range(team_size):
        print(f"\nCreating hero #{i+1}:")
        hero = Superhero()
        print(hero)
        team.append(hero)
    
    print(f"\n🏆 {team_name} - YOUR SUPER TEAM 🏆")
    for i, member in enumerate(team, 1):
        print(f"\nHero #{i}:")
        print(member)
    
    print("\nGo save the world!")

if __name__ == "__main__":
    main()