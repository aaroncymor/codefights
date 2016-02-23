chessBoard = [[True,True,False,False], 
			 [False,False,True,False], 
			 [False,False,False,False], 
			 [True,False,False,False], 
			 [False,False,False,False], 
			 [False,False,False,False], 
			 [False,True,True,False], 
			 [False,True,True,True]]


def rooksOnChessBoard(chessBoard):
	rows = len(chessBoard)
	columns = len(chessBoard[0])

	for i in range(len(chessBoard)):
		for j in range(len(chessBoard[i])):
			if chessBoard[i][j] == True:
				r = i + 1
				while r < rows:
					if chessBoard[r][j] == True:
						return False
					r += 1
				c = j + 1
				while c < columns:
					if chessBoard[i][c] == True:
						return False
					c += 1
	return False

print(rooksOnChessBoard(chessBoard))