from abc import ABC, abstractmethod


class Animal(ABC):
    
    @abstractmethod #Indicate that method eat is abastract
    def eat(self):
       print('Animal is eating ...')
    
#Note: Abstract class: is a class with at least one abstract method (method without body).
# We can't create objects from Abstract classes.

class Duck(Animal):
    def eat(self):
        print('Duck is eating ...')
        super().eat()

duck = Duck()
duck.eat()