class Feline():
    
    def __init__(self, name, age, species):
        # Constructor: defines the attributes of the feline
        self.name = name
        self.age = age
        self.species = species
    
    def make_sound(self):
        # Method that describes the sound the feline makes
        return f"{self.name} makes a sound typical of its specie: {self.species}."

    def sleep(self):
        # Method to describe the feline sleeping
        return f"{self.name} is sleeping."

    def info(self):
        # Method to display information about the feline
        return f"Name: {self.name}, Age: {self.age}, Species: {self.species}"