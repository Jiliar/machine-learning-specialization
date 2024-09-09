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