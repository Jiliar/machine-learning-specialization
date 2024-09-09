class Animal:
    
    def __init__(self, name):
        self.name = name


class Duck(Animal):
    
    def __init__(self, name):
        super().__init__(name)
    
    def swim(self):
        print(f'{self.name} is swimming like a Duck with two legs...')

class Dog(Animal):
    
    def __init__(self, name):
        super().__init__(name)
    
    def swim(self):
        print(f'{self.name} is swimming like a Dog with four legs...')
        
class Fish(Animal):

    def __init__(self, name):
        super().__init__(name)
    
    def swim(self):
        print(f'{self.name} is swimming like a Fish with fins...')
    

def swim(animal):
    animal.swim()

duck = Duck('Lucas')
dog = Dog('Bobby')
fish = Fish('Nemo')

swim(duck)
swim(dog)
swim(fish)


