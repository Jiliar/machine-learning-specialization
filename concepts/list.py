list1 = [1,2,3,4]
list2 = [5,6,7,8]
list1.append(list2)
print(list1)

# output: 1, 2, 3, 4, [5, 6, 7, 8]]

listA = [1,2,3,4]
listB = [5,6,7,8]
listA += listB
print(listA)

# output: [1, 2, 3, 4, 5, 6, 7, 8]

listA.insert(10,'m')
print(listA)

# output: [1, 2, 3, 4, 5, 6, 7, 8, 'm']

listB.sort(reverse = True)
print(listB)
# output: [8, 7, 6, 5]

listA.pop()
print(listA)

# output: [1, 2, 3, 4, 5, 6, 7, 8]

listA.remove(2)
print(listA)

# output: [1, 3, 4, 5, 6, 7, 8]

del(listA[0])
print(listA)

# output: [3, 4, 5, 6, 7, 8]

print(listA[:-1])
# output: [3, 4, 5, 6, 7]

print(listA[-1])
# output: 8

x = 1
print(x in listA)
# output: False

print(listA + listB)
#output: [3, 4, 5, 6, 7, 8, 8, 7, 6, 5]

i,j=1, -2
print(listA[i:j])
#output: [4, 5, 6]

print(listA * 2)
#outpt: [3, 4, 5, 6, 7, 8, 3, 4, 5, 6, 7, 8]

print(len(listA))
#outpt: 6

print(min(listA))
#outpt: 3

print(max(listA))
#outpt: 8