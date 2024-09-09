#Basic Lambda Functions:

addition = lambda x,y: x+y
print(f'Suma: {addition(3,5)}')

data = [1, 2, 3, 4]
squares = lambda data: [x ** 2 for x in data]
print(squares(data))  

# output: [1, 4, 9, 16]

#Lambda Functions in Higher Order Functions:

# map():

numbers = [1,2,3,4]
squares = list(map(lambda x:x**2, numbers))
print(squares)

# filter():

numbers = [1,2,3,4,5]
pares = list(filter(lambda x: x%2 == 0, numbers))
print(pares)

# sorted():
tuples = [(1, 'uno'), (3, 'tres'), (2, 'dos')]
sorted_values = sorted(tuples, key=lambda x:x[1])
print(sorted_values)

#Lambda Functions with Conditional Expressions

max_value = lambda x, y: x if x > y else y
print(max_value(5,10))