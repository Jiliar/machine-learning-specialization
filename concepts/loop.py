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

print(result[0:-2])

#output: 0, 1, 9, 16, 25, 36, 49