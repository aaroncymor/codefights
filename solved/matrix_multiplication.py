def MatrixMultiplication(matrixA, matrixB):
	colALen, rowALen = len(matrixA[0]), len(matrixA)
	colBLen, rowBLen = len(matrixB[0]), len(matrixB)

	if colALen != rowBLen:
		return "Can't multiply."

	#Create container for product of the 2 matrices.rowALen x colBLen
	product = []
	for i in range(rowALen):
		product.append([0] * colBLen)

	i, j = 0,0
	x, y = 0,0
	while i < rowALen:
		s = 0
		k = 0
		while j < colALen:
			if k < colBLen:
				#print "a: ",i, j,"b: ",j, k
				s += matrixA[i][j] * matrixB[j][k]
				if j == (colALen - 1):
					
					if y < len(product[0]) and x < len(product):
						product[x][y] = s
					
					if y == len(product[0]) - 1:
						y = 0
						x += 1
					else:
						y += 1
					k += 1
					j,s = 0,0
				else:
					j += 1
			else:
				break;

		i += 1
	return product

print MatrixMultiplication([[1,2,3],[4,5,6],[7,8,1]],[[1,2,3],[3,2,1],[4,5,2]])
print MatrixMultiplication([[1,4,6]],[[2,3],[5,8],[7,9]])
print MatrixMultiplication([[6,3,0],[2,5,1],[9,8,6]],[[7,4],[6,7],[5,0]])