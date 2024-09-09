class Fish:
    
    def __init__(self, weight, height, __type):
        self.weight = weight # public convention
        self._height = height # private convention
        self.__type = __type #name magling: Python interpreter change the name of variable to avoid collisions or overriding
    
    def _swim(self): # If start with underscore '_' private access convention
        print('Swiming like a Fish!')

fish = Fish(5.5, 30, 'Pargo')
print(dir(fish), sep='\n')
print(f'fish weight: {fish.weight}')
print(f'fish height: {fish._height}')
print(f'fish type: {fish._Fish__type}')