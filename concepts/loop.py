result = ''
for x in range(10):
    if x == 0:
        pass # Non defined code
    if x == 8:
        break # break loop
    if x == 2:
        continue # start loop again, Non execute: line 6, 7
    value = x * x
    result += str(value) + ', '

print(result[0:-2], sep='\n')

#output: 0, 1, 9, 16, 25, 36, 49

lista1 = [10,99,80, 124,3]

for x in range(0, len(lista1)):
    print(lista1[x], end=' ')

#output: 0, 1, 9, 16, 25, 36, 49

print('\n')

for element in lista1:
    print(element, end=' ')
#output: 10 99 80 124 3

print('\n')

for element in reversed(lista1):
    print(element, end=' ')
#output: 3 124 80 99 10

print('\n')

for element in sorted(lista1, reverse=True):
    print(element, end=' ')

#output: 124 99 80 10 3

print('\n')

for element in sorted(lista1):
    print(element, end=' ')

#output: 3 10 80 99 124