"""
You are given a n x m matrix, which contains all the integers 
from 1 to n * m, inclusive, each exactly once.

Initially you are standing in the cell containing the number 1. 
On each turn you are allowed to move to an adjacent cell, i.e. 
to a cell that shares a common side with the one you are standing
on now. It is prohibited to visit any cell more than once.

Check if it is possible to visit all the cells of the matrix 
in the order of increasing numbers in the cells, i.e. get to 
the cell with the number 2 on the first turn, then move to 3, etc.

[
[1,4]
[2,5]
[3,6]
]

[
[1,2]
[3,4]
[5,6]
]

[[1,5,9], 
 [2,6,10], 
 [3,7,11], 
 [4,8,12]]
"""

def findPath(matrix):
	check_horizontally = True

	if len(matrix) > 1:
		if matrix[0][0] < matrix[1][0]:
			if (matrix[1][0] - 1) == matrix[0][0]:
				check_horizontally = False
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if check_horizontally and j + 1 < len(matrix[i]):
				if matrix[i][j] != matrix[i][j + 1] - 1:
					return False
			elif not check_horizontally:
				if i + 1 < len(matrix):
					if matrix[i][j] != matrix[i + 1][j] - 1:
						return False
	return True

print findPath([[1,2],[3,4],[5,6]])
print findPath([[1,4],[2,5],[3,6]])
print findPath([[1,5,9],[2,6,10],[3,7,11],[4,8,12]])
print findPath([[1,3,2]])