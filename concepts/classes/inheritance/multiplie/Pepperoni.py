from Pizza import Pizza

class Pepperoni(Pizza):
    
    def __init__(self, size, crust_type, drink=None):
        # Automatically set the default ingredients for Hawaiian pizza: ham and pineapple
        super().__init__(size, crust_type)
        self.drink=drink

    def get_free_drink(self):
        return f"Drink {self.drink}."