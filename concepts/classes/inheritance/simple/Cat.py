from Feline import Feline


class Cat(Feline):
    
    def __init__(self, name, age, breed):
        # Call the Feline base class constructor
        super().__init__(name, age, "Gato")
        self.breed = breed  # Adds the specific breed attribute for the Cat class

    def purr(self):
        return f"{self.name} is purring."

    def scratch(self):
        return f"{self.name} is scratching the furniture."


cat = Cat('Kitty', 2, 'Fish')

print(cat.make_sound())
print(cat.sleep())
print(cat.info())
print(cat.purr())
print(cat.scratch())
