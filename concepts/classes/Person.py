class Person:
    
    #Class Variables
    calories = 0.0

    
    def __init__(self, name, lastname, age, weight_grs, height_mts, city, country, weariness, hunger, thirst):
        print('<< init >>')
        # Instance variables
        self.name = name
        self.lastname = lastname
        self.age = age
        self.weight_grs = weight_grs
        self.height_mts = height_mts
        self.city = city
        self.country = country
        self.weariness = weariness
        self.hunger = hunger
        self.thirst = thirst
        
#Note: __init__ is a method to init instance variable (it is a kind of constructor for programming languages like Java)

    #Instance Method #1: eat
    def eat(self):
        print('eating...')
        self.weight_grs = 1.5
        self.hunger = 0.0
    
    #Instance Method #2: sleep
    def sleep(self):
        print('sleping...')
        self.weariness = 0.0
    
    #Instance Method #3: drink
    def drink(self):
        print('drinking...')
        self.thirst = 0.0

#Note: Through the word "self" you can identify when a method is an instance.

    @classmethod
    def run(cls):
        print('running...')
        cls.hunger = 5.0
        cls.thirst = 8.0

#Note: Class methods can be called without instantiating objects. cls is a reference of class methods.
#  @classmethod is a decorator to indicate special cases.

    @staticmethod
    def jumping():
        print('jumping...')
        calories = 6.0

#Note: Static methods can be called without instantiating objects and without Class reference. 
#decorator @staticmethod is mandatory and it doesn't use self o cls.
#This kind of method doesn't have access to instance and class methods


#Creating instances
person1 = Person("Alice", "Smith", 30, 70.0, 1.70, "New York", "USA", 0.2, 0.1, 0.3)
print(f'Name: {person1.name}')
print(f'Country: {person1.country}')

#Instance method
print(f'Eat:')
person1.eat()

#Class method
print(f'Run:')
Person.run()

#Static Method
print(f'Jump:')
Person.jumping()