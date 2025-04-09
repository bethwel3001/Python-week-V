import time
from random import choice

class Animal:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        raise NotImplementedError("Subclasses must implement this!")
    
    def speak(self):
        raise NotImplementedError("Subclasses must implement this!")

class Cheetah(Animal):
    def move(self):
        return f"{self.name} the Cheetah sprints at 70 mph! 🏃💨"
    
    def speak(self):
        return "Purrr-chirp! (Yes, cheetahs chirp like birds!) 🐆"

class Penguin(Animal):
    def move(self):
        return f"{self.name} the Penguin waddles cutely! 🐧"
    
    def speak(self):
        return "Noot noot! 🎺"

class Dolphin(Animal):
    def move(self):
        return f"{self.name} the Dolphin swims with graceful flips! 🐬"
    
    def speak(self):
        return "Eee-eee-click! (Dolphin sonar sounds) 📡"

class Vehicle:
    def __init__(self, model):
        self.model = model
    
    def move(self):
        raise NotImplementedError("Subclasses must implement this!")
    
    def honk(self):
        raise NotImplementedError("Subclasses must implement this!")

class RaceCar(Vehicle):
    def move(self):
        return f"{self.model} zooms past with a VROOM! 🏎️💨"
    
    def honk(self):
        return "Beep-beep! (But more like a Formula 1 horn) 🏁"

class HotAirBalloon(Vehicle):
    def move(self):
        return f"{self.model} floats gently with the wind 🎈"
    
    def honk(self):
        return "... (silence, because balloons don't have horns) 🤫"

class MonsterTruck(Vehicle):
    def move(self):
        return f"{self.model} CRUSHES everything in its path! 🚚💥"
    
    def honk(self):
        return "HONK HOOOONK! (Airhorn blast) 📢"

def animate_text(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()

def main():
    print("🌟" * 25)
    animate_text("Welcome to the Polymorphism Zoo & Vehicle Showcase!")
    print("🌟" * 25 + "\n")
    
    # Create our polymorphic collection
    entities = [
        Cheetah("Lightning"),
        Penguin("Waddles"),
        Dolphin("Splash"),
        RaceCar("Speedy"),
        HotAirBalloon("Sky Wanderer"),
        MonsterTruck("Crusher")
    ]
    
    while True:
        print("\nWhat would you like to see?")
        print("1. Animal Movement Showcase 🐾")
        print("2. Vehicle Movement Showcase 🚀")
        print("3. Full Interactive Demo! 🎮")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == "1":
            print("\n" + "🐾" * 30)
            animate_text("ANIMAL MOVEMENT SHOWCASE!")
            for entity in entities[:3]:  # Just animals
                animate_text(entity.move())
                animate_text(f"...and says: {entity.speak()}")
                print("-" * 40)
        
        elif choice == "2":
            print("\n" + "🚗" * 30)
            animate_text("VEHICLE MOVEMENT SHOWCASE!")
            for entity in entities[3:]:  # Just vehicles
                animate_text(entity.move())
                animate_text(f"...and honks: {entity.honk()}")
                print("-" * 40)
        
        elif choice == "3":
            print("\n" + "🎮" * 30)
            animate_text("INTERACTIVE DEMO TIME!")
            
            # Let user create their own
            entity_type = input("\nCreate an animal or vehicle? (a/v): ").lower()
            
            if entity_type == "a":
                name = input("Name your animal: ")
                animal_type = choice(["cheetah", "penguin", "dolphin"])
                
                if animal_type == "cheetah":
                    entity = Cheetah(name)
                elif animal_type == "penguin":
                    entity = Penguin(name)
                else:
                    entity = Dolphin(name)
                
                animate_text(f"\nCreated {name} the {animal_type.capitalize()}!")
            
            elif entity_type == "v":
                model = input("Name your vehicle: ")
                vehicle_type = choice(["race car", "hot air balloon", "monster truck"])
                
                if vehicle_type == "race car":
                    entity = RaceCar(model)
                elif vehicle_type == "hot air balloon":
                    entity = HotAirBalloon(model)
                else:
                    entity = MonsterTruck(model)
                
                animate_text(f"\nCreated {model} {vehicle_type.capitalize()}!")
            
            else:
                print("Invalid choice! Let's pick a random one for you!")
                entity = choice(entities)
            
            # Interact with the created entity
            while True:
                print("\nWhat would you like to do?")
                print("1. Make it move")
                print("2. Make it speak/honk")
                print("3. Go back to main menu")
                
                action = input("Choose action (1-3): ")
                
                if action == "1":
                    animate_text("\n" + entity.move())
                elif action == "2":
                    if isinstance(entity, Animal):
                        animate_text("\n" + entity.speak())
                    else:
                        animate_text("\n" + entity.honk())
                elif action == "3":
                    break
                else:
                    print("Invalid choice! Try again.")
        
        elif choice == "4":
            animate_text("\nThanks for visiting the Polymorphism Zoo & Vehicle Showcase!")
            animate_text("Remember: In programming as in life, different objects can share the same interface!")
            print("🌟" * 25)
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()