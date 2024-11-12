from abc import ABC, abstractmethod
from typing import List

class GameCharacter(ABC):
    """Abstract base class for all game characters"""
    
    def __init__(self, name: str, health: int, level: int = 1):
        self._name = name
        self._health = health
        self._max_health = health
        self._level = level
        self._experience = 0
        self._inventory: List[str] = []
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def health(self) -> int:
        return self._health
    
    def add_to_inventory(self, item: str) -> None:
        self._inventory.append(item)
        print(f"{self._name} picked up {item}!")
    
    def show_stats(self) -> None:
        print(f"\n{self._name}'s Stats:")
        print(f"Level: {self._level}")
        print(f"Health: {self._health}/{self._max_health}")
        print(f"Inventory: {', '.join(self._inventory) if self._inventory else 'Empty'}")
    
    @abstractmethod
    def special_ability(self) -> None:
        """Each character type must implement their unique special ability"""
        pass

class Warrior(GameCharacter):
    def __init__(self, name: str, weapon: str):
        super().__init__(name, health=120)  # Warriors have high health
        self._weapon = weapon
        self.add_to_inventory(weapon)
    
    def special_ability(self) -> None:
        print(f"{self._name} uses Battle Cry! Damage increased!")
        
    def charge_attack(self) -> None:
        print(f"{self._name} charges forward with their {self._weapon}!")

class Mage(GameCharacter):
    def __init__(self, name: str, element: str):
        super().__init__(name, health=80)  # Mages have lower health
        self._element = element
        self.add_to_inventory("Magic Staff")
        
    def special_ability(self) -> None:
        print(f"{self._name} casts an {self._element} explosion!")
        
    def cast_spell(self, spell_name: str) -> None:
        print(f"{self._name} casts {spell_name} using {self._element} magic!")

class Rogue(GameCharacter):
    def __init__(self, name: str):
        super().__init__(name, health=90)  # Rogues have medium health
        self.add_to_inventory("Dagger")
        self._stealth = True
        
    def special_ability(self) -> None:
        print(f"{self._name} vanishes into the shadows!")
        
    def backstab(self) -> None:
        if self._stealth:
            print(f"{self._name} performs a devastating backstab!")
            self._stealth = False
        else:
            print(f"{self._name} must be stealthy to backstab!")

# Example usage
def main():
    # Create different character types
    warrior = Warrior("Ragnar", "Battle Axe")
    mage = Mage("Merlin", "frost")
    rogue = Rogue("Shadow")
    
    # Demonstrate polymorphism with special abilities
    characters = [warrior, mage, rogue]
    print("Each character using their special ability:")
    for character in characters:
        character.special_ability()
    
    print("\nDemonstrating unique class methods:")
    warrior.charge_attack()
    mage.cast_spell("Blizzard")
    rogue.backstab()
    
    # Show stats for all characters
    for character in characters:
        character.show_stats()

if __name__ == "__main__":
    main()