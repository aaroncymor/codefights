"""
Lisa likes to play sudoku in her free time. However, since she only solves sudokus that are published in the local newspaper, she can check her solutions only by manually checking each row, column and subgrid, which is super boring.

Your job is to help Lisa by writing a program which accepts a 9 × 9 matrix and determines if it follows sudoku rules. Each row, column and a 3 × 3 subgrid in the matrix must contain all digits from 1 to 9 with no repetitions.

Example

For

s = [[5,3,4,6,7,8,9,1,2], 
     [6,7,2,1,9,5,3,4,8], 
     [1,9,8,3,4,2,5,6,7], 
     [8,5,9,7,6,1,4,2,3], 
     [4,2,6,8,5,3,7,9,1], 
     [7,1,3,9,2,4,8,5,6], 
     [9,6,1,5,3,7,2,8,4], 
     [2,8,7,4,1,9,6,3,5], 
     [3,4,5,2,8,6,1,7,9]]
the output should be
Sudoku(s) = true.

The given sudoku is correct.

Input/Output

[time limit] 4000ms (py)
[input] array.array.integer s

A 9 × 9 matrix containing integers from 1 to 9.

[output] boolean

true if the given sudoku is correct, false otherwise.
"""

def sudoku(matrix):
	l = []
	for i in range(3):
		for j in range(9):
			for k in range(i*3,(i + 1) * 3):
				l.append(matrix[j][k])
			if len(l) == 9:
				#print(l)
				if len(set(l)) != 9:
					return False
				else:
					l = []
	l1, l2 = [],[]	
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			l1.append(matrix[i][j])
			l2.append(matrix[j][i])
		print(l1,l2)
		if(len(set(l1)) != 9 and len(set(l2)) != 9):
			return False
	return True

s =[[5,3,4,6,7,8,9,1,2], 
 [6,7,2,1,9,5,3,4,8], 
 [1,9,8,3,4,2,5,6,7], 
 [8,5,9,7,6,1,4,2,3], 
 [4,2,6,8,5,3,7,9,1], 
 [7,1,3,9,2,4,8,5,6], 
 [9,6,1,5,3,7,2,8,4], 
 [2,8,7,4,1,9,6,3,5], 
 [3,4,5,2,8,6,1,7,9]]

print(sudoku(s))