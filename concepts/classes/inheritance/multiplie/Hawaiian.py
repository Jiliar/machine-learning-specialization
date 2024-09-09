from Pizza import Pizza

class Hawaiian(Pizza):
    
    def __init__(self, size, crust_type, chef=None):
        # Automatically set the default ingredients for Hawaiian pizza: ham and pineapple
        super().__init__(size, crust_type)
        self.chef = chef

    def get_chef(self):
        return f"Chef {self.chef}."