class Pizza:
    
    def __init__(self, size, crust_type):
        # Constructor: defines the attributes of the pizza
        self.size = size  # Size of the pizza (e.g., "small", "medium", "large")
        self.crust_type = crust_type  # Type of crust (e.g., "thin", "thick", "whole wheat")
        

    def get_price(self):
        # Method to calculate the price of the pizza based on size and number of ingredients
        base_price = {"small": 8, "medium": 10, "large": 12}
        return base_price[self.size]

    def display_info(self):
        # Method to display information about the pizza
        return f"Pizza size: {self.size}, Crust: {self.crust_type}, Price: ${self.get_price()}"
