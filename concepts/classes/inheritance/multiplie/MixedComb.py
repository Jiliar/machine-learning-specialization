from Hawaiian import Hawaiian
from Pepperoni import Pepperoni
from Pizza import Pizza

class MixedComb(Hawaiian, Pepperoni):
    
    def __init__(self, size, crust_type, chef, drink):
        Hawaiian.__init__(self, size, crust_type, chef)
        Pepperoni.__init__(self, size, crust_type, drink)
    
mixed = MixedComb('large', 'thin', 'Chef Luigi', 'Coke')

print(mixed.display_info())
print(mixed.get_price())
print(mixed.get_free_drink())
print(mixed.get_chef())
        