def count_up_to(n):
    counter = 1
    while counter <= n:
        yield counter  # Pause here and return the counter value
        counter += 1

# Using the generator
generator = count_up_to(5)

# Iterate through the values ​​produced by the generator
for number in generator:
    print(number, end= ' ')

print('\n')

def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

# Use generator
for numero in fibonacci(10):
    print(numero, end= ' ')