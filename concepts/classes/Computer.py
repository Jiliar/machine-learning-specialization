class Computer:
    
    def __init__(self):
        model = ''
        brand = ''
    
    def sell(self):
        self.model = 'MacBook Pro 14'
        self.brand = 'Mac'
    
    def sell(self):
        self.model = 'MacBook Air'
        self.brand = 'Mac'

computer = Computer()
computer.sell()
print(computer.model)

# Run the latest python method
# Method overloading does not exist in python because:
# - Dynamically Typed: Python is a dynamically typed language, meaning that the types of variables are determined at run time, not at compile time.
# - Flexible argument handling: Python has a different way of handling multiple function signatures through features like default parameters.
# - Function overriding: If you try to define multiple versions of a method with the same name, the latest definition will override the previous ones.