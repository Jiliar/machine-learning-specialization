# Functions without params

def greetings():
    print('¡Hello!')

greetings()
# output: ¡Hello!


# Functions with params

def greetings(name:str):
    print(f'¡Hello {name}! ')

name = 'Juan'
greetings(name)
# output: ¡Hello Juan!

# Note: if call greetings() without args it will an error, because the function definition has changed.

# Functions that return values

def greetings(name:str, lastname:str):
    return f'¡Hello {name} {lastname}! '

lastname = 'Alvarez'
print(greetings(name, lastname))
# output: ¡Hello Juan Alvarez!


# Functions with params with default values

def greetings(name:str = 'Juan', lastname:str = 'Alvarez', age:int = 18):
    return f'¡Hello {name} {lastname}! you are {age} years old.'

print(greetings())
# output: ¡¡Hello Juan Alvarez! you are 18 years old.!

# Functions with params with names

x =  greetings( lastname = 'Pacheco', age = 23, name = 'Carlos')
print(x)
# output: ¡Hello Carlos Pacheco! you are 23 years old.

# Function with a dynamic number of parameters.

def counter(x, *numbers):
    value = ''
    
    print(f'arguments: ')
    print(f'x: {x} ')
    print(f'numbers: {numbers} ')
    
    for n in numbers:
        value += str(n) + ', '
    return f'output: {x}, {value[:-2]}'

print(counter(1,2,3))
# output: 1, 2, 3

