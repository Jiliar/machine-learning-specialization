a = 1
b = a
c = b
print(f' a: {a} b: {b} c: {c}')
#output: a: 1 b: 1 c: 1

a,b,c = 10,11,12
print(f' a: {a} b: {b} c: {c}')
#output: a: 10 b: 11 c: 12

print(a,b,c, sep = ' - ')
#output: 10 - 11 - 12