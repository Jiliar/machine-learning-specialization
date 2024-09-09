list1 = [1,2,3,4]
list2 = [5,6,7,8]
matrix = [list1, list2]
print(matrix)
# output: [[1, 2, 3, 4], [5, 6, 7, 8]]

print(matrix[1][3])
# output: 8

list1.append(9)
matrix = [list1, list2]
print(matrix)
# output: [[1, 2, 3, 4, 9], [5, 6, 7, 8]]

print(matrix[0][4])
# output: 9